#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 16:37
# @Author  : wkend
# @File    : test2.py
# @Software: PyCharm

import sys
import getopt


def main(argv):
    file_name = sys.argv[0]
    print('file_name:'+file_name)


if __name__ == '__main__':
    main(sys.argv[1:])