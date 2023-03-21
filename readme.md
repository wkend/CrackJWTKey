# JWT秘钥爆破脚本

## 说明
支持签名算法为`HS256`的密钥爆破
## 用法
```python
python3 -m pip install -r requirements.txt

python3 CrackJWT.py jwt_str keys.txt

```
## 示例
```
PS C:\tools\redTeam\passCrack\CrackJWTKey-master\CrackJWTKey-master\CrackJWT> python3 .\CrackJWT.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzkzNzM3NjYsInVzZXJuYW1lIjoiMTIzNHF3ZXIifQ.voh3bgfKO46Om8s7yQBlyaD2YXnQXjUa5lQyGXrlecQ .\keys.txt

                              _        ___  _    _  _____
                             | |      |_  || |  | ||_   _|
      ___  _ __   __ _   ___ | | __     | || |  | |  | |
     / __|| '__| / _` | / __|| |/ /     | || |/\| |  | |
    | (__ | |   | (_| || (__ |   <  /\__/ /\  /\  /  | |
     \___||_|    \__,_| \___||_|\_\ \____/  \/  \/   \_/
                                                          (v 1.1)

[-] try key --> 000000
[-] try key --> 1234
[-] try key --> 123456
[-] try key --> 12345678
[-] try key --> user
[-] try key --> test
[+] found key successfully!!!  --> secret

```
## 参考
https://www.freebuf.com/vuls/211842.html
