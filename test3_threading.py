# _*_coding: utf-8 _*_
import time
import threading
from multiprocessing import Pool

# 创建简单的进程


def printthreading(num):
    time.sleep(1)
    print("线程:{}".format(num))
    return


for i in range(10):
    t = threading.Thread(target=printthreading,
                         args=(i,), name="线程{}".format(i))
    t.start()

# 演示进程锁
lock = threading.RLock()


def printnumber1(gNumber):
    time.sleep(1)
    print(gNumber)


def printnumber2(gNumber):
    lock.acquire()
    time.sleep(1)
    print(gNumber)
    lock.release()


for i in range(5):
    t = threading.Thread(target=printnumber1, args=(i,))
    t.start()

time.sleep(1)
for j in range(5):
    t = threading.Thread(target=printnumber2, args=(j,))
    t.start()

# 进程池


def f0(i):
    time.sleep(0.5)
    print("apply f0:", i)
    return i + 100


def f1(i):
    time.sleep(0.5)
    print("apply_async f1:", i)
    return i + 100


def f2(arg):
    print("apply_asunc f2", arg)


print('*', end='')

if __name__ == '__main__':
    pool = Pool(10)
    for i in range(1, 3):
        pool.apply(func=f0, args=(i,))

    for i in range(4, 6):
        pool.apply_async(func=f1, args=(i,), callback=f2)
    pool.close()
    pool.join()
print('?', end='')
