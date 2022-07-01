import matplotlib.pyplot as plt
import numpy as np
from sympy import false, true

# T[i, j] = (T[i+1, j] + To[i-1, j] + To[i, j+1] + To[i, j-1])/4
time = 30
te = 20
L = 0.8
n = 40
a = 0.016
s = 0.1
dx = L/n
dy = dx
dt = s/(a*(1/dx**2 + 1/dy**2))

x = np.linspace(0, L, n)
y = np.linspace(0, L, n)

T = 30 * np.ones([n, n]) 

T[0:n-1, 0] = te
T[0:n-1, n-1] = te
T[0, 0:n-1] = te
T[n-1, 0:n-1] = te

# calc
m = int(n/2)
size = int(m/4)

plt.figure(dpi=300)
plt.ylim([-0.02,0.82])
plt.xlim([-0.02, 0.82])
X, Y = np.meshgrid(x, y)

t = 0
t1 = False
t2 = False
t3 = False
while t <= time:
    To = T.copy()
    
    for j in range(1, n-1):
        for i in range(1, n-1):
            T[i, j] = To[i, j] + dt*a*(((To[i-1, j] - 2*To[i, j] + To[i+1, j])/dx**2) + ((To[i, j-1] - 2*To[i,j] + To[i, j+1])/dy**2))
            for k in range(int(n/4)):
                T[m-size+k, m-size:m+size] = 100
    t += dt
    if t >= 10 and t1 == False:
        t1 = True
        graf = plt.contour(X, Y, T, 9, vmin=20, vmax=100, linewidths=1, cmap='rainbow')
        plt.clabel(graf, fontsize=5)
        plt.show()
    elif t >= 20 and t2 == False:
        t1 = True
        graf = plt.contour(X, Y, T, 9, vmin=20, vmax=100, linewidths=1, cmap='rainbow')
        plt.clabel(graf, fontsize=5)
        plt.show()
    elif t >= 30 and t3 == False:
        graf = plt.contour(X, Y, T, 9, vmin=20, vmax=100, linewidths=1, cmap='rainbow')
        plt.clabel(graf, fontsize=5)
        plt.show() 
