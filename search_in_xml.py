# -*- coding: utf-8 -*-
#python3
import re
import os
def get_file_list(fpath):
    """获得fpath目录下的所有xml文件
    """
    if not os.path.isdir(fpath): return
    lst = os.listdir(fpath)
    n = len(lst)
    for i in range(n):
        full_path = fpath + '//' + lst[i]
        lst[i] = full_path
    file_list = []
    while len(lst) != 0:
        sec_path = lst.pop(0)
        if os.path.isfile(sec_path): 
            f = open(sec_path, 'rb')
            first5 = tuple(f.read(5))
            if first5 == (0x3c, 0x3f, 0x78, 0x6d, 0x6c):
                file_list.append(sec_path)
            f.close()
        else:
            sec_ls = os.listdir(sec_path)
            for i in sec_ls:
                lst.append(sec_path + '//' + i)
    return file_list
    
def build_file_show_lst(f_lst):
    """将双斜杠改为单斜杠
    """
    n = len(f_lst)
    for i in range(n):
        f_lst[i] = re.sub('//', '/', f_lst[i])
    return f_lst
        
    
def get_sens_list(f_list, pattern):
    """f_list is a list of files, pattern is a regex expression.
        this function returns a list of files which matches pattern.
    """ 
    sens_list = []
    for i in f_list:
        if not os.path.isfile(i): continue
        f = open(i, 'r')
        for line in f:
            m = re.search(pattern, line)
#            m = re.search('\\blibhunspell\\b', line)
            if m is not None:
                sens_list.append(i)
                break
        f.close()
    return build_file_show_lst(sens_list)
          
fpath = '//home//lord//Downloads//codeblocks-16.01.release'
lst = get_file_list(fpath)
pat = '\\bVCLibrarianTool\\b'
f_ls = get_sens_list(lst, pat)
print(f_ls)
