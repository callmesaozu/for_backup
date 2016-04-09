# -*- coding: utf-8 -*-
import re
import os
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
    
def get_sens_list(f_list, pattern):
    """f_list is a list of files, pattern is a regex expression.
        this function returns a list of files which matches pattern.
    """ 
    sens_list = []
    for i in f_list:
        if not os.path.isfile(i): continue
        f = open(i, 'r')
        for line in f:
            m = re.search(pattern, line, re.I)
            if m is not None:
                sens_list.append(i)
                break
        f.close()
    return sens_list
          
fpath = '//home//lord//lord//data//aclImdb//test//pos'
lst = get_file_list(fpath)
patd = '\\bnoise\\b'
f_lsd = get_sens_list(lst, patd)
#patb =  '\\bbirth\\b'
#f_lsb = get_sens_list(lst, patb)
#print('dead')
print(f_lsd)
#print('birth')
#print(f_lsb)
