import matplotlib.pyplot as plt
import numpy as np


#算術平均
def mean(num):
    m = sum(num) / len(num)

#中央値
def median(num):
  num = sorted(num)
  if len(num) % 2 == 0:
      me = (num[int(len(num)/2-1)] + num[int(len(num)/2)]) / 2
      print(me)
  else:
      me = r[len(num)//2]
      print(me)

#最頻値()
def mode(num):
    dic = {}
    for i in num:
        if i not in dic.keys():
            dic.setdefault(i,1)
        else:
            dic.update({i:dic[i]+1})
    v = max(dic.values())
    for i in dic:
        if dic[i] == v:
            print(i,v)

#分散
def variance(num):
    m  = sum(num) / len(num)
    x = 0
    for i in num:
        x += (i - m)**2
    s2 = x/len(num)
    print(s2)

#標準偏差
def standard_deviation(num):
    m  = sum(num) / len(num)
    x = 0
    for i in num:
        x += (i - m)**2
    s = (x/len(num))**0.5
    print(s)

#標準化
def standardization(num):
    m  = sum(num) / len(num)
    x = 0
    for i in num:
        x += (i - m)**2
    s = (x/len(num))**0.5
    for i in num:
        print((i - m) / s)

#共分散
def covariance():
    # r1 = np.random.randint(0,100,100)
    # r2 = np.random.randint(0,100,100)
    r1 = [36,73,51,80]
    r2 = [90,57,36,17]
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
    # r1 = np.random.randint(0,100,100)
    # r2 = np.random.randint(0,100,100)
    r1 = [12,38,28,50,76]
    r2 = [28,35,55,87,93]
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
    cor = c / s
    print(cor)
    plt.scatter(r1,r2)
    plt.show()


if __name__ == '__main__':
    num = np.random.randint(0,100,100)
    mean(num)
    median(num)
    mode(num)
    variance(num)
    standard_deviation(num)
    standardization(num)
