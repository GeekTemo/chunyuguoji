#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by gongxingfa on 16/3/18

from multiprocessing import Process
from Crypto.Cipher import AES
from Crypto.Hash import MD5

maby_chars = ['ycjJGqZdRNP6FPKTTg==', 'iImIW+cfBZK7VbPSD8aAtQSu']
comb_chars = ['', '&', '|', '+']
cipher_text = 'FaY0KZCkULdIPpcTCzzSEnhrsyPRTlX4BQFvUU0NfFbYphXDk5SO5Nwy1zCFs6vej90to+qgpmG1jWKP8TAuVGHiv9XLbd8fNEMVCMI9MamYAUHxVUJM5a+AiPd+H2kbZTqu6iGl31P5KKkQvRiUJrdlbQgWBG9jcC1h7DMrPZAm+gYO\/GiAXyUKFX+HYfX6Gw79y85YSm0o+lFP+kYErUKhP9CEXGdzxHnYfO\/Phbw+dMMacSgebiUQ4HY8gBXPC3zTOBvGh+Dg\/GtKq8XGov1gHfTaVTxlkv4YIOcunPFHkQOZAb0qNzySWo8ZYkevavny0\/zuHqWwipi8WGnNqSfGeH1leHX4HkcwNP4hc18W19T\/AaQFuV\/ANoYJSdQeTlKKMlOXJCG1sCV9ucRQpG8PNdBeyxGdTpg1eQYhKvKQBx0b38CyhGzkCpa0O8y8Syq+rclB1cdifmWqUv2ugXFZ\/1ZMaKHRsEAco4V\/+lcL9AtUngRQE4SnF+jbk9jpYwLoIphZZe\/2lITTkNeaZNfJ7vHcGW6qud\/I1LvPUNHzzVEBq5AM4VDNMHY5u8niSxJkt0vJBXpcBS9Dy5sU7nCUHL8xpPRVySxuiqvChpovAgw6PUySeVdRfnvjUwvbQsJZPfzReguhdwf6hv44Q2cqjvTxdF\/BWjzUybHtxhhL7ixrTgpyTmKVYWaR7iycQo3WliaR9anxOc4WP2V7xeljtvq\/XvINf9U\/TFhMRv73G0CPzWE0f9Bl5k5cpYFD3zrFZ2DcfDStNh7r7\/bq55qwO3R3mfS968YtzVSCOhx7an0tbYgle0faSvZvB9ZG6Q+WmpDOvdzuRWPZbiGWSvUEKo2PQnBpr7lVAhqtlAfY6OWcS4YiVKpIYJBb6wvKpFasxwzdHN4PZvbTolvZONctvHiaKi+D9kFVHgi2slmBXSaiuDUL6l5Dg+SSPFv3GevEiVvEKgURklqI+tOoZ76XpZLsWAPU888hlwHmBjxhipupDnpBhfGu\/vQOtwaTBYJxgeTumoKeJkAY3gqB5\/DWL+75eTCZPX2bH2zpTEw4FT+xZ9ufiZL4OWzjtPpn'


# PublishID APP id    (ycjJGqZdRNP6FPKTTg==) 20位
# PlacementID 广告ID  (Banner:iImIW+cfBZK7VbPSD8aAtQSu) 24位 可单独作为AES_192密钥

# 方法一 AES_192 24位
# 直接用 PlacementID作为密钥

# 方法二 AES_256 32位
# 密钥 =  MD5(comb(PublishID,PlacementID)) 32位字符串作为密钥 组合关键的一些字符
# 密文 =  AES(密钥, 明文)



# 方法三 DES 16 24 32位密钥
# 密钥 =  方法二中的MD5截取8位字符

def comb_key():
    for comb_char in comb_chars:
        yield maby_chars[1]
        for maby_char in maby_chars:
            yield maby_chars[0] + comb_char + maby_chars[1]


class Cracker(Process):
    def __init__(self, ciphertext):
        Process.__init__(self)
        self.ciphertext = ciphertext

    def aes_decrp(self, secret):
        obj = AES.new(secret)
        return obj.decrypt(self.ciphertext)

    def run(self):
        m = MD5.new()
        for key in comb_key():
            m.update(key)
            secret = m.hexdigest()
            msg = self.aes_decrp(secret)
            print 'Key:', key
            print 'Secret:', secret
            print 'Msg:', msg
            print '-----' * 50


def _start_crack():
    cracker = Cracker(cipher_text)
    cracker.start()


if __name__ == '__main__':
    _start_crack()
