#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 16:52
# @Author  : wkend
# @File    : test3.py
# @Software: PyCharm

import sys
from termcolor import colored, cprint

# text = colored('Hello, World!', 'grey', attrs=['reverse', 'blink'])
text = colored('Hello, World!', 'grey', attrs=['reverse'])
print(text)


# cprint('Hello, World!', 'green', 'on_red')
#
# print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
# print_red_on_cyan('Hello, World!')
# print_red_on_cyan('Hello, Universe!')
#
# for i in range(10):
#     cprint(i, 'magenta', end=' ')
#
# cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)