#!/usr/bin/env python 3.5
# -*- coding: utf-8 -*-

class CommonLine():
    _text = '''
                          _        ___  _    _  _____ 
                         | |      |_  || |  | ||_   _|
  ___  _ __   __ _   ___ | | __     | || |  | |  | |  
 / __|| '__| / _` | / __|| |/ /     | || |/\| |  | |  
| (__ | |   | (_| || (__ |   <  /\__/ /\  /\  /  | |  
 \___||_|    \__,_| \___||_|\_\ \____/  \/  \/   \_/  
                                                      
github: https://github.com/wkend/CrackJWTKey                                                    
'''
    def __init__(self,argvs=None):
        pass

    def run(self):
        print(self._text)



def main():
    try:
        cmd = CommonLine()
        cmd.run()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
