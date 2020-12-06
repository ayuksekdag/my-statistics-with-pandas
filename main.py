#descriptive statistics

import pandas as pd
dataset1 = [15,18,25,16,14,20]
dataset2 = [2,3,3,23,38,39]
dataset3 = [3,18,16,15,16,40]
dataset4 = [17,18,19,17,18,19]
dataset5 = [18,18,18,18,18,18]

d1_s = pd.DataFrame(dataset1)
d2_s = pd.DataFrame(dataset2)
d3_s = pd.DataFrame(dataset3)
d4_s = pd.DataFrame(dataset4)
d5_s = pd.DataFrame(dataset5)

d1_sum = d1_s.describe()
d2_sum = d2_s.describe()
d3_sum = d3_s.describe()
d4_sum = d4_s.describe()
d5_sum = d5_s.describe()

print ('dataset 1',d1_s.transpose())
print ('dataset 2',d2_s.transpose())
print ('dataset 3',d3_s.transpose())
print ('dataset 4',d4_s.transpose())
print ('dataset 5',d5_s.transpose())

print ('dataset 1\n',d1_sum.transpose())
print ('dataset 2\n',d2_sum.transpose())
print ('dataset 3\n',d3_sum.transpose())
print ('dataset 4\n',d4_sum.transpose())
print ('dataset 5\n',d5_sum.transpose())

