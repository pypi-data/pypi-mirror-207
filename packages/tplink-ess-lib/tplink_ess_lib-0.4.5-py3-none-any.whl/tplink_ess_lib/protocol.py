"""Provide protocol encode/decoding functions."""

import base64
import logging
import struct
from ipaddress import ip_address

from .binary import byte2ports, mac_to_str

_LOGGER = logging.getLogger(__name__)


class Protocol:
    """Class to handle TpLink ESS messages."""

    PACKET_END = b"\xff\xff\x00\x00"

    KEY_BASE64 = """
        v5vjymOiT2gxEr6kHky9gxc0VmrPfX6pxBysOryEoAMkeJCoDOd0LClhbNUqxiCU2mv3cMwOQkRb
        4M7rIYLLsgGGx075eweRSdDRZEpzSHYIFvOTQGAFVzxx6Zgf24+u6Jn1nv5GqktN19M7R4XWnZcG
        LlFeiKbSBCvxHd+wQz+6iYEo+P83Dz633mnsxX82s8LluSVa7bgZnK0au9wC4QDwMvvU/acRwc2x
        FbX2UuImZaO28lwUC18N5hB5fG3DdSdi71Q4i6EvyTOH+goTli1vGxiOUFVT6orYOV1Bmo16IoyA
        7lhZCZKrlTVmPXJF2a9n5CO0/MjApZ/d9G53MA==
    """

    KEY = base64.b64decode(KEY_BASE64)

    header = {
        "len": 32,
        "fmt": "!bb6s6shihhhhi",
        "blank": {
            "version": 1,
            "op_code": 0,
            "switch_mac": b"\x00\x00\x00\x00\x00\x00",
            "host_mac": b"\x00\x00\x00\x00\x00\x00",
            "sequence_id": 0,
            "error_code": 0,
            "check_length": 0,
            "fragment_offset": 0,
            "flag": 0,
            "token_id": 0,
            "checksum": 0,
        },
    }

    DISCOVERY = 0
    GET = 1
    SET = 2
    LOGIN = 3
    RETURN = 4
    READ5 = 5

    op_codes = {
        DISCOVERY: "DISCOVERY",
        GET: "GET",
        SET: "SET",
        LOGIN: "LOGIN",
        RETURN: "RETURN",
        READ5: "READ5",
    }

    sequences = {
        # name      ->switch    switch->
        "login/change": (LOGIN, RETURN),
        "query": (GET, SET),
        "discover": (DISCOVERY, SET),
    }

    ids_tp = {
        1: ("str", "type", 0),
        2: ("str", "hostname", 1, "Without arguments, shows switch details"),
        3: ("hex", "mac", 0),
        4: ("ip", "ip_addr", 0),
        5: ("ip", "ip_mask", 0),
        6: ("ip", "gateway", 0),
        7: ("str", "firmware", 0),
        8: ("str", "hardware", 0),
        9: ("bool", "dhcp", 0),
        10: ("dec", "num_ports", 0),
        12: ("bool", "led_status", 0),
        13: ("bool", "auto_save", 0),
        14: ("bool", "is_factory", 0),
        15: ("hex", "flash_type", 0),
        512: ("str", "username", 0),
        514: ("str", "password", 0),
        773: ("bool", "reboot", 1, "Reboot the device"),
        2304: ("action", "save", 1, "Saves the current configuration"),
        2305: ("action", "get_token_id", 1, "Unknown"),
        4352: ("bool", "igmp_snooping", 0),
        4096: ("hex", "ports", 0),
        4608: ("hex", "trunk", 0),
        8192: ("hex", "mtu_vlan", 0),
        8704: ("hex", "vlan_enabled", 0),
        8705: ("vlan", "vlan", 1, "Configure VLAN Membership"),
        8706: ("pvid", "pvid", 0),
        8707: ("str", "vlan_filler", 0),
        12288: ("bool", "qos1", 0),
        12289: ("hex", "qos2", 0),
        16640: ("hex", "mirror", 0),
        16384: ("stat", "stats", 0),
        17152: ("bool", "loop_prev", 0),
    }

    tp_ids = {v[1]: k for k, v in ids_tp.items()}

    @staticmethod
    def get_id(name):
        """Return id from name."""
        return Protocol.tp_ids[name]

    @staticmethod
    def decode(data):
        """Decode switch packet."""
        data = bytearray(data)
        s = bytearray(Protocol.KEY)  # pylint: disable=invalid-name
        j = 0
        for k in range(len(data)):  # pylint: disable=consider-using-enumerate
            i = (k + 1) & 255
            j = (j + s[i]) & 255
            s[i], s[j] = s[j], s[i]
            data[k] = data[k] ^ s[(s[i] + s[j]) & 255]
        return bytes(data)

    encode = decode

    @staticmethod
    def split(data):
        """Split the packet apart."""
        if len(data) < Protocol.header["len"] + len(Protocol.PACKET_END):
            raise AssertionError("invalid data length")
        if not data.endswith(Protocol.PACKET_END):
            raise AssertionError("data without packet end")
        return data[0 : Protocol.header["len"]], data[Protocol.header["len"] :]

    @staticmethod
    def interpret_header(header):
        """Decode the packet header."""
        names = Protocol.header["blank"].keys()
        vals = struct.unpack(Protocol.header["fmt"], header)
        return dict(zip(names, vals))

    @staticmethod
    def interpret_payload(payload):
        """Decode the packet payload."""
        results = []
        while len(payload) > len(Protocol.PACKET_END):
            dtype, dlen = struct.unpack("!hh", payload[0:4])
            data = payload[4 : 4 + dlen]
            results.append(
                (
                    dtype,
                    Protocol.ids_tp[dtype][1],
                    Protocol.interpret_value(data, Protocol.ids_tp[dtype][0]),
                )
            )
            payload = payload[4 + dlen :]
        return results

    @staticmethod
    def assemble_packet(header, payload):
        """Build packet from header and payload."""
        payload_bytes = b""
        for dtype, value in payload:
            payload_bytes += struct.pack("!hh", dtype, len(value))
            payload_bytes += value
        header["check_length"] = (
            Protocol.header["len"] + len(payload_bytes) + len(Protocol.PACKET_END)
        )
        header = tuple(header[part] for part in Protocol.header["blank"])
        header_bytes = struct.pack(Protocol.header["fmt"], *header)
        return header_bytes + payload_bytes + Protocol.PACKET_END

    @staticmethod
    def interpret_value(value, kind):
        """Decode payload values."""
        if kind == "str":
            value = value.split(b"\x00", 1)[0].decode("ascii")
        elif kind == "ip":
            value = f"{ip_address(value):s}"
        elif kind == "hex":
            value = mac_to_str(value)
        elif kind == "action":
            value = "n/a"
        elif kind == "dec":
            value = int.from_bytes(value, "big")
        elif kind == "vlan":
            value = list(
                struct.unpack("!hii", value[:10]) + (value[10:-1].decode("ascii"),)
            )
            value[1] = byte2ports(value[1])
            value[2] = byte2ports(value[2])
        elif kind == "pvid":
            value = struct.unpack("!bh", value) if value else None
        elif kind == "stat":
            value = struct.unpack("!bbbIIII", value)
        elif kind == "bool":
            if len(value) == 0:
                pass
            elif len(value) == 1:
                value = value[0] > 0
            else:
                raise AssertionError("boolean should be one byte long")
        return value

    @staticmethod
    def set_vlan(vlan_num, member_mask, tagged_mask, vlan_name):
        """Set vlan entry."""
        value = (
            struct.pack("!hii", vlan_num, member_mask, tagged_mask)
            + vlan_name.encode("ascii")
            + b"\x00"
        )
        return value

    @staticmethod
    def set_pvid(vlan_num, port):
        """Set port primary vlan ID."""
        value = struct.pack("!bh", port, vlan_num)
        return value
