import numpy as np
a = np.asarray([1,2,3,4])
b = np.asarray([6,7,8,9])
c = np.stack(a,b)
print(c)