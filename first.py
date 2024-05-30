import os
import numpy as np
import matplotlib.pyplot as plt
import csv

def f(x):
    return -20*np.exp(-0.2*np.sqrt(0.5*(x**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+1))+np.e+20

start = -5
end = 5
step = 0.01

x = np.arange(start, end, step)

y = f(x)

plt.plot(x, y,'r')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции y = f(x)')
plt.grid(True)
plt.show()

data = [['Number', 'x', 'f(x)']]
for i, (val_x, val_y) in enumerate(zip(x, y)):
    data.append([i+1, val_x, val_y])

directory = 'results'
if not os.path.exists(directory):
    os.makedirs(directory)
file_path = os.path.join(directory, 'results.csv')

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print(f'Data saved to {filename}')


