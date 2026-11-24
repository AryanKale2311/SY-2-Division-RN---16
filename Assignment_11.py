import pandas as pd
import numpy as np

s = pd.Series(np.random.randint(1, 100, 10))

print("Series:")
print(s)

print("Indexing:", s[2])

print("Filtering:")
print(s[s > 50])

print("Mean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())
