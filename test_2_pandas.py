import pandas as pd
import numpy as np

x = pd.Series(range(5))
print(x)


x = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4})
print(x)
print()

x = np.array([range(4), range(2, 10, 2)])
y = pd.DataFrame(x)
print(y)
print()

x = {"0": [1, 2, 3], "1": [2, 3, 4], "3": [3, 4, 5], "4": [4, 5, 6]}
y = pd.DataFrame(x)
print(y)
print()

x = {"0": {'1': 1, '2': 2, '3': 3}, "1": {'1': 2, '2': 4, '3': 6}}
y = pd.DataFrame(x)
print(y)
print()


x = {"0": {'1': 1, '2': 2, '3': 3}, "1": {
    '1': 2, '2': 4, '3': 6}, "2": {'1': 3, '2': 6, '3': 9}}
y = pd.DataFrame(x)
z = y[['0', '1', '2']]
print(z)
print()
