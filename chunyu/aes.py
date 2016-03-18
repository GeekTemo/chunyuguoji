#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gongxingfa on 16/3/18


# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import os
import base64

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

#key = os.urandom(16) # the length can be (16, 24, 32)
#text = 'to be encrypted'
key = '12345678901234567890123456789012' # the length can be (16, 24, 32)
#text = '1234567890123456'
#text = '1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
text = '中文坎坎坷坷吞吞吐吐yy语音男男女女'

cipher = AES.new(key)

#encrypted = cipher.encrypt(pad(text)).encode('hex')
encrypted = cipher.encrypt(pad(text))
print encrypted  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'
result = base64.b64encode(encrypted)
print result  # will be something like 'f456a6b0e54e35f2711a9fa078a76d16'

#decrypted = unpad(cipher.decrypt(encrypted.decode('hex')))
result2 = base64.b64decode(result)
print result2  # will be 'to be encrypted'
decrypted = unpad(cipher.decrypt(result2))
print decrypted  # will be 'to be encrypted'