# _*_ coding:utf-8 _*_
import csv
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from functools import partial

csvfile = r"./Students_score.csv"

# 随机生成成绩
with open(csvfile, 'w+') as fp:
    wr = csv.writer(fp)
    wr.writerow(["学号", "Python", "Java", "C"])
    for i in range(1000000):
        wr.writerow([str(i + 1), random.randrange(101),
                     random.randrange(101), random.randrange(101)])

# 分段统计人数
nleft = 0
nright = 0

df = pd.read_csv(csvfile, encoding="utf-8").dropna(axis=0)
plt.figure()
x = df["Python"]
y = df["Java"]
z = df["C"]
l_x = list(x)
l_y = list(y)
l_z = list(z)
ly = list(range(101))


def f(s, nleft, nright):
    if s < nright and s >= nleft:
        return 1
    else:
        return 0


# 制图
area = [0, 60, 85, 101]
ly = [60, 85, 100]
total_x = [0, 0, 0]
total_y = [0, 0, 0]
total_z = [0, 0, 0]
for i in range(len(area) - 1):
    total_x[i] = sum(map(partial(f, nleft=area[i], nright=area[i+1]), l_x))
    total_y[i] = sum(map(partial(f, nleft=area[i], nright=area[i+1]), l_y))
    total_z[i] = sum(map(partial(f, nleft=area[i], nright=area[i+1]), l_z))
plt.plot(ly, total_x)
plt.title("Python_avg")
plt.savefig(r"./分段成绩统计_Python.png")
plt.plot(ly, total_y)
plt.title("Java_avg")
plt.savefig(r"./分段成绩统计_Java.png")
plt.plot(ly, total_z)
plt.title("C_avg")
plt.savefig(r"./分段成绩统计_C.png")


data = pd.read_csv(csvfile, encoding='utf-8')
list_csv = data.values.tolist()

# 平均数
avg_Python = sum(l_x) / 1000000
avg_Java = sum(l_y) / 1000000
avg_C = sum(l_z) / 1000000

# 方差
s_Python = 0
s_Java = 0
s_C = 0

for i in range(1000000):
    s_Python += (l_x[i] - avg_Python) ** 2
    s_Java += (l_y[i] - avg_Java) ** 2
    s_C += (l_z[i] - avg_C) ** 2

# 表格
sheet = {"AVG": {'Python': avg_Python, 'Java': avg_Java, 'C': avg_C},
         "VAR": {'Python': s_Python / 1000000, 'Java': s_Java / 1000000, 'C': s_C / 1000000}}
sheets = pd.DataFrame(sheet)
print(sheets)
