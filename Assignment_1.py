import matplotlib.pyplot as plt

from time import perf_counter

import random

import numpy as np


x = range(0,400)

matrix_size = x
time_taken=[]


for number in matrix_size:
    start = perf_counter()
    w=[]
    z=[]
    for s in range(number):
        a_row=[]
        b_row=[]
        for i in range(number):
            a_row.append(random.randint(0,9))
            b_row.append(random.randint(0,9))
        w.append(a_row)
        z.append(b_row)

        
    result=[[sum(x*y for x,y in zip(row_a,col_b)) for col_b in zip(*z)]for row_a in w]
    end = perf_counter()
    time_taken_run = end - start
    time_taken.append(time_taken_run)
print(time_taken)


print("Total Time is",sum(time_taken),"seconds")

x_points = np.array(matrix_size)
y_points = np.array(time_taken)

plt.plot(x_points, y_points)
plt.show()




