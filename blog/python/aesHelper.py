#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self, key='keyskeyskeyskeys', iv='0000000000000000'):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 这里密钥key 长度必须为16（AES-128）,24（AES-192）,或者32 （AES-256）Bytes 长度,目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            text = text + ('\0' * add)
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')


if __name__ == '__main__':
    a = prpcrypt()
    print a.encrypt('default') == '2db6d011ec8c41dc0708f0233c86e6e8'
    print a.decrypt('2db6d011ec8c41dc0708f0233c86e6e8')
    print a.encrypt('cmbchina') == '89ebee27974a776907d96074f555724b'
    print a.decrypt('89ebee27974a776907d96074f555724b')
    print a.encrypt(
        'cmbchinacmbchinacmbchinacmbchina') == '9ebcebe058e0343a4411b0fa50f4dfc75b9b75812c71f462a4e8951fc88945a4736b68db2d1ab30df1e6d9bcf03704c2'
    print a.decrypt('9ebcebe058e0343a4411b0fa50f4dfc75b9b75812c71f462a4e8951fc88945a4736b68db2d1ab30df1e6d9bcf03704c2')
