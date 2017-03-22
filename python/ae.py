#coding=utf-8
try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET

import base64
import string
import random
import hashlib
import time
import struct
from Crypto.Cipher import AES
import sys
import socket
from binascii import b2a_hex, a2b_hex

class prpcrypt():
    def __init__(self,key):
        self.key = key
        self.mode = AES.MODE_CBC

    #加密函数，如果text不足16位就用空格补足为16位，
    #如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self,text):
        cryptor = AES.new(self.key,self.mode)
        #这里密钥key 长度必须为16（AES-128）,
        #24（AES-192）,或者32 （AES-256）Bytes 长度
        #目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length-count)
            #\0 backspace
            text = text + ('\0' * add)
        elif count > length:
            add = (length-(count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        #因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        #所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    #解密后，去掉补足的空格用strip() 去掉
    def decrypt(self,text):
        IV = 16 * '\x00'

        cryptor = AES.new(self.key,self.mode,IV)
        plain_text  = cryptor.decrypt(base64.b64decode(text))

        pad = ord(plain_text[-1])
        # 去掉补位字符串
        #pkcs7 = PKCS7Encoder()
        #plain_text = pkcs7.encode(plain_text)
        # 去除16位随机字符串
        content = plain_text[16:-pad]
        xml_len = socket.ntohl(struct.unpack("I",content[ : 4])[0])
        xml_content = content[4 : xml_len+4]
        from_appid = content[xml_len+4:]

        return xml_content

aes_key = 'TPTgHAfnx6siAmvA14iX82M5EuZW8Q5MyH5ZcnL9f8b'
encrypt_content = "R+1LqZSys57F74U87hCrB+rAjAJjDOxgEbykJZciGxiVc2CG6wgH6/RWHUdoD+X1xCa5Q0ePnYuOQf4rXP+MunyVFyVmaFwv6Thc9Cg+mestR96jBrPXXWRQOwgpuxsvoUj+q60oEEj7fprTrjlxGrRZyJ6Qd1DmYDDscodtD8DK1eS1rlUSKJXE+OAdWY21nly0Ahl+YUL3rJZFbE0/O64iQfxziKe1QD0bP8aXnq0oGl4ywPmnZdgPymOA+rO9bzeZA5v/mKcaw/UoFUzcUbhX8Y9EKA0blV8MfrEQF6MKo2d7zn7JupaLm4pDdJyeiXjimbIfGKGxdFpie0SYUT29n8dy9qsna4NEAVK2bv756PZOZ179E84+YjE9eb5S8IOFIQ4lwH0xEBo1svec0wQEmAXkOewh6nYba1JKKJySevgawjXFR59WV3EJ4qqj3+oeUabXji9wmdLhrgK55hsX/xnHZEMu8vbm9biCXZ677V6Tk1Yy2YnPbyjkBrFrd3l/cRfDrOt0Ma/XRHDioxWT60NRv1bMkPFXOukPqfHfBlrrdimgFCIIpCiTTuZ3WYBnwypjxYyctGG/mBPBRw=="

     def encrypt(self,text,appid):
        """对明文进行加密
        @param text: 需要加密的明文
        @return: 加密得到的字符串
        """
        # 16位随机字符串添加到明文开头
        text = self.get_random_str() + struct.pack("I",socket.htonl(len(text))) + text + appid
        # 使用自定义的填充方式对明文进行补位填充
        pkcs7 = PKCS7Encoder()
        text = pkcs7.encode(text)
        # 加密
        cryptor = AES.new(self.key,self.mode,self.key[:16])
        try:
            ciphertext = cryptor.encrypt(text)
            # 使用BASE64对加密后的字符串进行编码
            return ierror.WXBizMsgCrypt_OK, base64.b64encode(ciphertext)
        except Exception,e:
            #print e
            return  ierror.WXBizMsgCrypt_EncryptAES_Error,None