import json
import struct


def parse(data):
    str_value = json.dumps(data)
    byte_encode = str_value.encode('utf-8')
    len_bytes = struct.pack('>I', len(byte_encode))
    return len_bytes + byte_encode


def stringify(data):
    len_bytes = data[:4]
    length = struct.unpack('>I', len_bytes)[0]
    byte_encode = data[4:4 + length]
    str_value = byte_encode.decode('utf-8')
    return json.loads(str_value)
