import numpy as np
from scipy import stats
data=[99,86,87,88,111,86,103,87,94,78,77,85,86]
print("mean =", np.mean(data))
print("median =", np.median(data))
print("70 percentile is ",np.percentile(data,70))
print("standard deviation =",np.std(data))
print("variance =",np.var(data))
print("mode =",stats.mode(data))