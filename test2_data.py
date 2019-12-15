# _*_ coding:utf-8 _*_
import csv
import random
import pandas as pd
import matplotlib.pyplot as plt

csvfile = r"./score.csv"

# 随机生成成绩
with open(csvfile, 'w+') as fp:
    wr = csv.writer(fp)
    wr.writerow(["学号", "成绩"])
    for i in range(100000):
        wr.writerow([str(i + 1), random.randrange(101)])

nleft = 0
nright = 0


def flag(s):
    global nleft, nright
    if s < nright and s >= nleft:
        return 1
    else:
        return 0


df = pd.read_csv(csvfile, encoding="utf-8").dropna(axis=0)
plt.figure()
x = df["成绩"]
lx = list(x)
ly = list(range(101))


# 方法1
total = list(range(101))
for i in range(101):
    nleft = i
    nright = i + 1
    total[i] = sum(map(flag, lx))

plt.plot(ly, total)
print(total)
plt.show()

# 方法2
for i in range(101):
    total[i] = x.between(i, i).sum()
plt.plot(ly, total)
print(total)
plt.show()
