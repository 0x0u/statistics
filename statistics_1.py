import numpy as np

#算術平均
def mean():
  r_num = np.random.randint(0,100,100)
  a = 0
  for i in r_num:
    a += i
  m = a / len(r_num)
  print(m)

#中央値
def median():
  r = np.random.randint(0,100,100)
  r = sorted(r)
  if len(r) % 2 == 0:
      me = (r[int(len(r)/2-1)] + r[int(len(r)/2)]) / 2
      print(me)
  else:
      me = r[len(r)//2]
      print(me)

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

#分散
def variance():
    r = np.random.randint(0,100,100)
    m  = sum(r) / len(r)
    x = 0
    for i in r:
        x += (i - m)**2
    s2 = x/len(r)
    print(s2)

#標準偏差
def standard_deviation():
    r = np.random.randint(0,100,100)
    m  = sum(r) / len(r)
    x = 0
    for i in r:
        x += (i - m)**2
    s = (x/len(r))**0.5
    print(s)

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
    print(c)

#相関係数
def correlation():
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
    sx,sy = 0,0
    for s1,s2 in zip(r1,r2):
        sx += (s1 - m1)**2
        sy += (s2 - m2)**2
    s = ((sx/len(r1))**0.5) * ((sy/len(r1))**0.5)
    print(c / s)

mean()
median()
mode()
variance()
standard_deviation()
standardization()
covariance()
correlation()
