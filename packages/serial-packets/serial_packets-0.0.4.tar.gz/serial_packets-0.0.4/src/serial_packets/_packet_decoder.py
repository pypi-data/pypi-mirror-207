from __future__ import annotations

import logging
import asyncio
from PyCRC.CRCCCITT import CRCCCITT
from typing import Optional, Callable

from ._packets import PacketType, PACKET_FLAG, PACKET_ESC, MIN_PACKET_LEN, MAX_PACKET_LEN
from .packets import MAX_DATA_LEN
# from .packets import  PACKET_MAX_LEN

logger = logging.getLogger(__name__)


# class DecodedPacket:

#     def __init__(self, cmd_id: int, type: PacketType, endpoint: Optional(int),
#                  status: Optional(int), data: bytearray):
#         self.cmd_id = cmd_id
#         self.type = type
#         self.endpoint = endpoint
#         self.status = status
#         self.data = data

#     def __str__(self):
#         return f"{self.cmd_id}, {self.endpoint}, {len(self.data)}"

#     def dump(self, title="Decoded packet"):
#         print(f"{title}", flush=True)
#         print(f"  Cmd id   {self.cmd_id: 10d}", flush=True)
#         print(f"  Type   {self.type.name}", flush=True)
#         print(f"  Endpoint   {self.endpoint}", flush=True)
#         print(f"  Status   {self.status}", flush=True)
#         print(f"  Data: {self.data.hex(sep=' ')}", flush=True)


class DecodedCommandPacket:

    def __init__(self, cmd_id: int, endpoint: int, data: bytearray):
        self.cmd_id = cmd_id
        self.endpoint = endpoint
        self.data = data

    def __str__(self):
        return f"Command packet: {self.cmd_id}, {self.endpoint}, {len(self.data)}"


class DecodedResponsePacket:

    def __init__(self, cmd_id: int, status: int, data: bytearray):
        self.cmd_id = cmd_id
        self.status = status
        self.data = data

    def __str__(self):
        return f"Response packet: {self.cmd_id}, {self.endpoint}, {len(self.data)}"


class DecodedMessagePacket:

    def __init__(self, endpoint: int, data: bytearray):
        self.endpoint = endpoint
        self.data = data

    def __str__(self):
        return f"Message packet: {self.endpoint}, {len(self.data)}"



class PacketDecoder:

    def __init__(self, decoded_packet_callback: Callable[[DecodedPacket], None]):
        assert (decoded_packet_callback is not None)
        self.__crc_calc = CRCCCITT("FFFF")
        self.__packet_bfr = bytearray()
        self.__in_packet = False
        self.__pending_escape = False
        self.__packet_bfr.clear()
        self.__decoded_packet_callback = decoded_packet_callback
        # self.__packets_queue = asyncio.Queue()

    def __str__(self):
        return f"In_packet ={self.__in_packet}, pending_escape={self.__pending_escape}, len={len(self.__packet_bytes)}"

    def __reset_packet(self):
        # self.__state = state
        self.__in_packet = False
        self.__pending_escape = False
        self.__packet_bfr.clear()

    # async def get_next_packet(self):
    #     """Blocking asyncio fetch of next pending packet."""
    #     return await self.__packets_queue.get()

    def _receive(self, data: bytes):
        for b in data:
            self.__receive_byte(b)

    def __receive_byte(self, b: int):
        # If not already in a packet, wait for next flag.
        if not self.__in_packet:
            if b == PACKET_FLAG:
                # Start collecting a packet.
                self.__in_packet = True
                self.__pending_escape = False
                self.__packet_bfr.clear()
            return

        # Here collecting packet bytes. Handle end of packet.
        assert (self.__in_packet)
        if b == PACKET_FLAG and not self.__pending_escape:
            self.__process_packet()
            self.__reset_packet()
            # No need to wait for additional flag byte before next packet.
            self.__in_packet = True
            return

        # Check for size overrun. At this point, we know that the packet will
        # have at least one more additional byte.
        if len(self.__packet_bfr) >= MAX_PACKET_LEN:
            logger.error("Packet is too long (%d), dropping", len(self.__packet_bfr))
            self.__reset_packet()
            return

        # Handle escape byte
        if b == PACKET_ESC:
            if self.__pending_escape:
                logger.error("Two consecutive escape chars, dropping packet")
                self.__reset_packet()
            else:
                self.__pending_escape = True
            return

        # Handle escaped byte.
        if self.__pending_escape:
            b1 = b ^ 0x20
            if b1 != PACKET_FLAG and b1 != PACKET_ESC:
                logger.error("Invalid escaped byte (%02x, %02x), dropping packet", b1, b)
                self.__reset_packet()
            else:
                self.__packet_bfr.append(b1)
                self.__pending_escape = False
            return

        # Handle normal byte
        self.__packet_bfr.append(b)

    def __process_packet(self):
        rx_bfr = self.__packet_bfr

        # Ignore empty packets
        n = len(rx_bfr)
        if not n:
            # Zero length packet can occur normally when we insert
            # a pre packet flag.
            return

        # Check for minimum length. A minimum we should
        # have a type byte and two CRC bytes.
        if n < MIN_PACKET_LEN:
            logger.error("Packet too short (%d), dropping", n)
            return

        # Check CRC
        packet_crc = int.from_bytes(rx_bfr[-2:], byteorder='big', signed=False)
        computed_crc = self.__crc_calc.calculate(bytes(rx_bfr[:-2]))
        if computed_crc != packet_crc:
            logger.error("Packet CRC error %04x vs %04x, dropping", packet_crc, computed_crc)
            return

        # Construct decoded packet
        type_value = rx_bfr[0]
        if type_value == PacketType.COMMAND.value:
            cmd_id = int.from_bytes(rx_bfr[1:5], byteorder='big', signed=False)
            endpoint = rx_bfr[5]
            data = rx_bfr[6:-2]
            decoded_packet = DecodedCommandPacket(cmd_id,  endpoint,  data)
        elif type_value == PacketType.RESPONSE.value:
            cmd_id = int.from_bytes(rx_bfr[1:5], byteorder='big', signed=False)
            status = rx_bfr[5]
            data = rx_bfr[6:-2]
            decoded_packet = DecodedResponsePacket(cmd_id,  status, data)
        elif type_value == PacketType.MESSAGE.value:
            endpoint = rx_bfr[1]
            data = rx_bfr[2:-2]
            decoded_packet = DecodedMessagePacket(endpoint,  data)
        else:
            logger.error("Invalid packet type %02x, dropping packet", type.value)
            return

        if len(data) > MAX_DATA_LEN:
            logger.error("Packet data too long (type=%d, len=%d), dropping", type_value,
                         len(data))
            return

        # Inform the user about the new packet.
        self.__decoded_packet_callback(decoded_packet)

        # self.__packets_queue.put_nowait(decoded_packet)
