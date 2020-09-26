import json
import os


def hex_to_binary(string):
    n = int(string, 16)
    b_str = ''
    while n > 0:
        b_str = str(n % 2) + b_str
        n = n >> 1
    return b_str.zfill(4)


def convert_bitmap_to_active_bits(bitmap, position=1):
    active_bits = []
    for element in bitmap:
        for bit in hex_to_binary(element):
            if bit == '1':
                active_bits.append(position)
            position += 1
    return active_bits
