#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gongxingfa on 16/3/18



def ecrypt(self, ecryptText):
    try:
        cipherX = DES.new(self.key, DES.MODE_CBC, self.iv)
        pad = 8 - len(ecryptText) % 8
        padStr = ""
        for i in range(pad):
            padStr = padStr + chr(pad)
        ecryptText = ecryptText + padStr
        x = cipherX.encrypt(ecryptText)
        return x.encode('hex_codec').upper()
    except:
        return ""


def decrypt(self, decryptText):
    try:

        cipherX = DES.new(self.key, DES.MODE_CBC, self.iv)
        str = decryptText.decode('hex_codec')
        y = cipherX.decrypt(str)
        return y[0:ord(y[len(y) - 1]) * -1]
    except:
        return ""
