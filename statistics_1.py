from scipy import stats
import statistics as st
import numpy as np
import math

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
  r = np.random.randint(0,100,100)
  r = sorted(r)
  if len(r) % 2 == 0:
      me = (r[int(len(r)/2-1)] + r[int(len(r)/2)]) / 2
      nump = np.media(r)
      print(me,nump)
  else:
      me = r[len(r)//2]
      nump = np.median(r)
      print(me,nump)

#最頻値()
def mode():
    r = np.random.randint(0,100,100)
    dic = {}
    for i in r:
        if i not in dic.keys():
            dic.setdefault(i,1)
        else:
            dic.update({i:dic[i]+1})
    v = max(dic.values())
    for i in dic:
        if dic[i] == v:
            print(i,v)

    power = stats.mode(r)
    print(power)

#分散
def variance():
    r = np.random.randint(0,100,100)
    m  = sum(r) / len(r)
    x = 0
    for i in r:
        x += (i - m)**2
    s2 = x/len(r)
    nump = np.var(r)
    print(s2,nump)


#標準偏差
def standard_deviation():
    r = np.random.randint(0,100,100)
    m  = sum(r) / len(r)
    x = 0
    for i in r:
        x += (i - m)**2
    s = (x/len(r))**0.5
    nump = np.std(r)
    print(s,nump)

#標準化
def standardization():
    r = np.random.randint(0,100,100)
    m  = sum(r) / len(r)
    x = 0
    for i in r:
        x += (i - m)**2
    s = (x/len(r))**0.5
    for i in r:
        print((i - m) / s)

#共分散
def covariance():
    r1 = np.random.randint(0,100,100)
    r2 = np.random.randint(0,100,100)
    m1 = sum(r1) / len(r1)
    m2 = sum(r2) / len(r2)
    d1 = [i - m1 for i in r1]
    d2 = [i - m2 for i in r2]
    c = 0
    for c1,c2 in zip(d1,d2):
        c += c1 * c2
    c = c / len(r1)

    nump = np.cov([r1,r2])
    print(c)
    print(nump)

#相関係数
def correlation():
     
