import matplotlib.pyplot as plt
import numpy as np
import time 
def meio_da_chapa():
    meio = int(n/2)
    tamanho = int(meio*2/3)
    T[meio, meio:meio+tamanho] = Tb
    for k in range(tamanho):
        T[meio-tamanho+k, meio:meio+k] = Tb
        T[meio-tamanho+k, meio:meio-k:-1] = Tb
        T[meio+tamanho-k, meio:meio+k] = Tb
        T[meio:meio+k, meio-tamanho+k:meio] = Tb


def salvar_grafico(arquivo_nome, matrix, tempo):
    ax = plt.subplot()
    plt.xlabel('Eixo t')
    plt.ylabel('Eixo Y')
    plt.xlim([-0.02, 0.92])
    plt.ylim([-0.02, 0.92])
    plt.title(f'Chapa Plana (2): malha com n={n} e t={tempo}s')
    grafico = ax.contour(X, Y, matrix, 12, vmin=Te, vmax=Tb, linewidths=1, cmap='rainbow') 
    chapa = plt.Rectangle((0,0), L, L, edgecolor='lightgrey', facecolor='black')
    buraco = plt.Rectangle((0.45, 0.24), L/3, L/3, angle=45, edgecolor='lightgrey', facecolor='white')
    plt.gca().add_patch(chapa)
    plt.gca().add_patch(buraco)
    ax.clabel(grafico, fontsize=5, fmt ='%1.1f')
    plt.savefig(f'{arquivo_nome}{tempo}.png', dpi=200)
    ax.clear()


tempo_total = 30
Te = 20
Tb = 100
Ti = 30
L = 0.9
n = 11
a = 0.016
s = 0.1
dx = L/n
dy = dx
dt = s/(a*(1/dx**2 + 1/dy**2))

T = Ti * np.ones([n, n]) 
x = np.linspace(0, L, n)
y = np.linspace(0, L, n)

T[0:n-1, 0] = Te
T[0:n-1, n-1] = Te
T[0, 0:n-1] = Te
T[n-1, 0:n-1] = Te
meio_da_chapa()

imag_10s = True
imag_20s = True
t = 0
inicio = time.time()
while t <= tempo_total:
    To = T.copy()
    for j in range(1, n-1):
        for i in range(1, n-1):
            T[i, j] = To[i, j] + dt*a*(((To[i-1, j] - 2*To[i, j] + To[i+1, j])/dx**2) + ((To[i, j-1] - 2*To[i,j] + To[i, j+1])/dy**2))
            meio_da_chapa()
    t += dt
    
    if t >= 10 and imag_10s:
        imag_10s = False
        T10 = T.copy()
    elif t >= 20 and imag_20s:
        imag_20s = False
        T20 = T.copy()
    elif t >= 30:
        T30 = T.copy()

X, Y = np.meshgrid(x, y)
salvar_grafico('chapa_02_t', T10, 10)
salvar_grafico('chapa_02_t', T20, 20)
salvar_grafico('chapa_02_t', T30, 30)
print('tempo: {}  FIM'.format(time.time()-inicio))
