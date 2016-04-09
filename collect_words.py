# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 22:15:34 2016

@author: lord
"""

#这段程序收集一个文本数据中的词出现的数量
import os
import re
def get_file_list(fpath):
    if not os.path.isdir(fpath): return
    lst = os.listdir(fpath)
    n = len(lst)
    for i in range(n):
        full_path = fpath + '//' + lst[i]
        lst[i] = full_path
    file_list = []
    while len(lst) != 0:
        sec_path = lst.pop(0)
        if not os.path.isdir(sec_path): 
            file_list.append(sec_path)
        else:
            sec_ls = os.listdir(sec_path)
            for i in sec_ls:
                lst.append(sec_path + '//' + i)
    return file_list
#c = re.findall('(?<=(^|"|\\s))[a-z]+(?=(\\.|\\s|"))', A, re.I)
#c = re.sub('(\\<.*\\>)|\\?|"|\\.|[0-9]+', ' ', A);这句更好

def collect(fpath):
    """收集一个fpath目录下的词出现的数量
    """
    f_list = get_file_list(fpath)
    if len(f_list) == 0:
        return {}
    dct = {}
    for i in f_list:
        if not os.path.isfile(i): 
            continue
        f = open(i, 'r')
        for line in f:
            c = re.sub('(\\<.*\\>)|\\?|"|\\.|[0-9]+', ' ', line.lower())
            words = c.split()
            for word in words:
                if word not in dct:
                    dct[word] = 1
                else:
                    dct[word] += 1
        f.close()
    return dct
fpath = '//home//lord//lord//data//aclImdb//test//pos'
col = collect(fpath)
f = open('//home//lord//lord//test//col.dat', 'w')
for i in col.keys():
    f.write(i+':'+str(col[i])+'\n')
f.close()

        