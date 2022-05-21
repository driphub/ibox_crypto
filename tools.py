import base64
import math
import random
import time

from Cryptodome.Cipher import AES, PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Util.Padding import pad

from config import private_key, public_key


def __get_crypto_key(n=16):
    n = n if n else 32
    codes = "abcdefhijkmnprstwxyz123456789"
    code_len = len(codes)
    ck = ''
    for i in range(n):
        ck += codes[math.floor(random.random() * code_len)]

    return ck


def __decode_aes(data, encrypt_key):
    data = data.replace('-', '+').replace('_', "/")
    aes = AES.new(encrypt_key, AES.MODE_ECB)
    encrypt_data = base64.b64decode(data)
    decrypted_text = aes.decrypt(encrypt_data)
    return decrypted_text.decode('utf-8')


def __decode_rsa(data, private_key):
    encrypt_text = data.encode('utf-8')
    key = '-----BEGIN PRIVATE KEY-----\n{}\n-----END PRIVATE KEY-----\n'.format(private_key)
    rsa_key = RSA.importKey(key.encode('utf-8'))
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)
    return cipher.decrypt(base64.b64decode(encrypt_text), "decode error！")


def __encode_aes(data, ck):
    aes = AES.new(ck.encode('utf-8'), AES.MODE_ECB)
    pad_text = pad(data.encode('utf-8'), 16, style='pkcs7')
    decrypted_text = aes.encrypt(pad_text)
    encrypt_text = (base64.b64encode(decrypted_text)).decode()
    return encrypt_text.replace('/', '_').replace('+', "-")


def __encode_rsa(ck):
    key = '-----BEGIN PUBLIC KEY-----\n{}\n-----END PUBLIC KEY-----\n'.format(public_key)
    rsa_key = RSA.importKey(key.encode('utf-8'))
    cipher = Cipher_pkcs1_v1_5.new(rsa_key)  # 创建用于执行pkcs1_v1_5加密或解密的密码
    cipher_text = base64.b64encode(cipher.encrypt(ck.encode('utf-8')))
    return cipher_text.decode('utf-8')


def encrypt(data):
    ck = __get_crypto_key()
    return {
        'data': __encode_aes(data, ck),
        'encryptKey': __encode_rsa(ck)
    }


def decrypt(data, encryptKey):
    rsa = __decode_rsa(data=encryptKey, private_key=private_key)
    return __decode_aes(data=data, encrypt_key=rsa)
