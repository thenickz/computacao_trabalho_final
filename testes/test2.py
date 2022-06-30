import matplotlib.pyplot as plt
import numpy as np

# T[i, j] = (T[i+1, j] + To[i-1, j] + To[i, j+1] + To[i, j-1])/4
time = 1
te = 20
L = 0.8
n = 30
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

'''# void
T[46, 36:56] = 0
for k in range(11):
    T[36+k, 46:46+k] = 0
    T[36+k, 46-k:46] = 0

for p in range(11):
    T[56-p, 46:46+p] = 0
    T[56-p, 46-p:46] = 0'''

m = int(n/2)
size = int(m*2/3)
for k in range(size):
    T[m-size+k, m:m+k] = 100
    T[m-size+k, m:m-k:-1] = 100
    T[m+k, m-size:m+size] = 100
    T[m+k, m+size-k:m+size] = 30
    T[m+k, m-size:m-size+k+1] = 30
plt.contour(T)

plt.show()
