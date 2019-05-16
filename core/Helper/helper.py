#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 10:39:32 2019

@author: chiranz
"""


import hashlib


BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def hash160(s):
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()

# Mainly used for checksum


def hash256(s):
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def encode_base58(s):
    count = 0

    for c in s:
        if c == 0:
            count += 1
        else:
            break

    num = int.from_bytes(s, 'big')
    prefix = '1'*count
    result = ''
    while num > 0:
        num, mode = divmod(num, 58)
        result = BASE58_ALPHABET[mode] + result
    return prefix + result


def encode_base58_checksum(b):
    return encode_base58(b + hash256(b)[:4])


def decode_base58(s):
    num = 0
    for c in s:
        num *= 58
        num += BASE58_ALPHABET.index(c)
    combined = num.to_bytes(25, 'big')
    checksum = combined[-4:]

    if hash256(combined[:-4])[:4] != checksum:
        raise ValueError(
            f'bad address: {checksum}, {hash256(combined[:-4])[:4]}')
    return combined[1:-4]


def int_to_little_endian(n, length):
    return n.to_bytes(length, 'little')


def little_endian_to_int(b):
    return int.from_bytes(b, 'little')


def int_to_big_endian(n, length):
    return n.to_bytes(length, 'big')


def big_endian_to_int(b):
    return int.from_bytes(b, 'big')
