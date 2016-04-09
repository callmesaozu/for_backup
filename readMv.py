
#python2.7.3
import re
def read_mv(fpath):
  #f = open(fpath, 'r', encoding = 'lating-1')
  f = open(fpath, 'r')
  dct = {}
  for line in f:
      #matc = re.search('::.+::.*Children\'s', line)
    matc =  re.search('::.+::(.+)', line)
    if matc != None:
        gener = re.split('\|', matc.group(1))
        print(gener)
        for i in gener:
            if dct.has_key(i) is False:
                dct[i] = 1
            else:
                dct[i] += 1
  f.close()
  return dct

#fpath = '//home//lord//data//ml-1m//movies.dat'
#dct = read_mv(fpath)

lst = []
lst.append('name')
print(lst)
