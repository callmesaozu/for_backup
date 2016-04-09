#-*- coding:utf8 -*-
#python2.7.3
import re
import os
def find_simple_chinese(fname, re_str, func):
  #f = open(fpath, 'r', encoding = 'lating-1')
    if not os.path.isfile(fname): return
    f = open(fname, 'r')
    for line in f:
        matc =  func(re_str, line)     
        if matc != None:
            print line
    f.close()
          
fpath = '//home//lord//codes//test.txt'
re_st = '\\bman\\b'
func = re.search
dct = find_simple_chinese(fpath, re_st, func)
