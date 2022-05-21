import os
import sys

from config import VERSION
from tools import encrypt, decrypt

if __name__ == '__main__':
    print(f'当前版本：{VERSION}')
    args = sys.argv
    try:
        if args[1] == 'h':
            print('当前支持的命令如下!')
            print('e：加密，需要传入的对象为json字符串！')
            print('d：解密，参数一：data，参数二：encryptKey！')
        if len(args) == 3 and args[1] == 'e':
            result = encrypt(args[2])
            print(result)
        elif len(args) == 4 and args[1] == 'd':
            result = decrypt(args[2], args[3])
            print(result)
        else:
            print('无效命令！')
            print('----------------')
            print('当前支持的命令如下!')
            print('e：加密，需要传入的对象为json字符串！')
            print('d：解密，参数一：data，参数二：encryptKey！')
            print('----------------')
    except:
        print('无效命令！')
        print('----------------')
        print('当前支持的命令如下!')
        print('e：加密，需要传入的对象为json字符串！')
        print('d：解密，参数一：data，参数二：encryptKey！')
        print('----------------')
