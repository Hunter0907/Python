import matplotlib.pyplot as plt

from time import perf_counter

import random

import numpy as np


x = range(0,250)

matrix_size= x
time_taken=[]


for num in matrix_size:
    start = perf_counter()
    a=[]
    b=[]
    for j in range(num):
        a_row=[]
        b_row=[]
        for k in range(num):
            a_row.append(random.randint(0,9))
            b_row.append(random.randint(0,9))
        a.append(a_row)
        b.append(b_row)

        
    result=[[sum(x*y for x,y in zip(row_a,col_b)) for col_b in zip(*b)]for row_a in a]
    end = perf_counter()
    time_taken_run = end - start
    time_taken.append(time_taken_run)
print(time_taken)


print("Total Time is",sum(time_taken),"seconds")

xpoints = np.array(matrix_size)
ypoints = np.array(time_taken)

plt.plot(xpoints, ypoints)
plt.show()




