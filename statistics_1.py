import numpy as np
import statistics

#算術平均

def mean():
  r_num = np.random.randint(0,100,100)
  a = 0
  for i in r_num:
    a += i
  m = a / len(r_num)
  nump = np.mean(r_num)
  print(m,nump)

#中央値

def median():
  r_num = np.random.randint(0,100,100)

#最頻値()

def mode():
    r = np.random.randint(0,100,100)
    dic = {}
    for i in r:
        if i not in dic.keys():
            dic.setdefault(i,1)
        else:
            dic.update({i:dic[i]+1})
    mode = statistics.mode(r)
    print(mode,dic[mode])
    print(max(dic.values()))
mode()
