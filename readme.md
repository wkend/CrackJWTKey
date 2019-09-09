# JWT秘钥爆破脚本
## 用法
`CrackJWT.py jwt_str passwd`
## 示例
```
python3 CrackJWT.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmFuYS
IsImFjdGlvbiI6InVwbG9hZCJ9.56wwCrB9tIgmUnYpLPxkO8GYj1soCjuu_skTlbH_Gg8 ../test/passwd.txt

                              _        ___  _    _  _____
                             | |      |_  || |  | ||_   _|
      ___  _ __   __ _   ___ | | __     | || |  | |  | |
     / __|| '__| / _` | / __|| |/ /     | || |/\| |  | |
    | (__ | |   | (_| || (__ |   <  /\__/ /\  /\  /  | |
     \___||_|    \__,_| \___||_|\_\ \____/  \/  \/   \_/
                                                          (v 1.0)
[+] try key --> azyhuvhahxnzfedh ,,,,,,,,,,
[+] try key --> advadvsd ,,,,,,,,,,
[+] try key --> adca ,,,,,,,,,,
[+] try key --> advsdv ,,,,,,,,,,
[+] try key --> sfvs ,,,,,,,,,,
[+] try key --> fb ,,,,,,,,,,
[+] try key --> dsfbdfbdf ,,,,,,,,,,
[+] try key --> $admina$ ,,,,,,,,,,
[+] found key successfully--> $admin$

```
## 参考
https://www.freebuf.com/vuls/211842.html