# -*- coding: utf-8 -*-
# author = 'K0ctr'


"""
md5，base64等编码解码
"""
import base64
import hashlib
import binascii


def decode_base_all(s):
    """
    输入一个字符串，使用base64，base32，base16进行解码并输出
    :param s: 编码字符串
    :return: 可能的解码结果
    """
    b = bytes(s, "utf-8")
    try:
        b64 = base64.b64decode(b)
        print("base64", b64)
    except binascii.Error:
        print("It's not base64 encode.")
    try:
        b32 = base64.b32decode(b)
        print("base32", b32)
    except binascii.Error:
        print("It isn't base32 encode.")
    try:
        b16 = base64.b16decode(b)
        print("base16", b16)
    except binascii.Error:
        print("It's not base16 encode.")


def encode_md5(s):
    """
    将一个字符串进行md5编码
    :param s: 需编码的字符串
    :return: md5值
    """
    b = bytes(s, encoding='utf-8')
    """
    m = hashlib.md5()
    m.update(b)
    print(m.hexdigest())
    """
    print(hashlib.new('md5', b).hexdigest())


encode_md5("abc")
decode_base_all("JeZkLH0YaA==")
