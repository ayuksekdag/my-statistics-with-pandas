#
import pandas as pd
dataset1 = [15,18,25,16,14,20]
dataset2 = [15,18,25,16,14,20]
dataset3 = [15,18,25,16,14,20]
dataset4 = [15,18,25,16,14,20]
dataset5 = [15,18,25,16,14,20]

d1_s = pd.Series(dataset1)
d2_s = pd.Series(dataset1)
d3_s = pd.Series(dataset1)
d4_s = pd.Series(dataset1)
d5_s = pd.Series(dataset1)

d1_sum = d1_s.describe()
print (d1_sum)