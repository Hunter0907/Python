import matplotlib.pyplot as plt
from time import perf_counter
import random
import numpy as np


x = range(0,400)

matrix_size = x
time_taken = []


for number in matrix_size:
    start = perf_counter()
    z=[]
    w=[]
    for j in range(number):
        row1=[]
        row2=[]
        for k in range(number):
            row1.append(random.randint(0,9))
            row2.append(random.randint(0,9))
        z.append(row1)
        w.append(row2)

        
    result=[[sum(x*y for x,y in zip(row1,row2)) for row2 in zip(*w)]for row1 in z]
    end = perf_counter()
    time_taken_run = end - start
    time_taken.append(time_taken_run)
print(time_taken)


print("Total Time is",sum(time_taken),"seconds")

x_points = np.array(matrix_size)
y_points = np.array(time_taken)

plt.plot(x_points, y_points)
plt.show()
