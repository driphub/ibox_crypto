# 某Box Nft Web数据加密解密脚本

## 运行方式

直接运行

```shell
pip3 install -r requirement.txt // 更新依赖
source venv/bin/active // 切py环境
python3 crypto.py d data encryptKey // 解密
python3 crypto.py e '{test: 123}' //加密
```

打包成二进制文件运行

```
pyinstaller -F crypto.py
cd dist/ && ./crypto d data encryptKey // 解密
cd dist/ && ./crypto e '{test: 123}' //加密
```

## Todo

x_use_c 待解密 包含了浏览器指纹
