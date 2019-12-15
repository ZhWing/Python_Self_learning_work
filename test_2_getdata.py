import pandas as pd
import numpy as np

'''
x = pd.Series(range(100))
print(x.values[2:6])
print()
'''
x = {"a": {'1': 1, '2': 2, '3': 3},
     "b": {'1': 2, '2': 4, '3': 6},
     "c": {'1': 3, '2': 6, '3': 9}}
y = pd.DataFrame(x)
y["d"] = {'1': 4, '2': 8, '3': 12}
print(y.a)
print(y["a"])
print(y.loc['1'])
print(y.head(2))
print()
print(y.tail(2))
