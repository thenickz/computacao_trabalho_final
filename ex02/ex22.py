import matplotlib.pyplot as plt
import numpy as np
import time 


# configurando variáveis
tempo_total = 30
Te = 20 # temperatura na extremidade
Ti = 30 # temperatura inicial da chapa
Tb = 100 # temperatura do buraco central
L = 0.9 # tamanho do lado da chapa
n = 21 # valor de n da malha
a = 0.016
s = 0.1
dx = L/n
dy = dx
dt = s/(a*(1/dx**2 + 1/dy**2))

# configurando vetores e matriz
x = np.linspace(0, L, n)
y = np.linspace(0, L, n)
T = Ti * np.ones([n, n]) # Ti deixa o valor inicial em toda a matriz

# aplicando as temperaturas nas extremidades
T[0:n-1, 0] = Te
T[0:n-1, n-1] = Te
T[0, 0:n-1] = Te
T[n-1, 0:n-1] = Te
# aplicando as temperaturas no buraco da chapa
def meio_da_chapa():
    meio = int(n/2) # metade do tamanho da chapa
    tamanho = int(meio*2/3) # tamanho do buraco
    T[meio, meio:meio+tamanho] = Tb
    for k in range(tamanho):
        T[meio-tamanho+k, meio:meio+k] = Tb
        T[meio-tamanho+k, meio:meio-k:-1] = Tb
        T[meio+tamanho-k, meio:meio+k] = Tb
        T[meio:meio+k, meio-tamanho+k:meio] = Tb


meio_da_chapa()
# iniciar método de euler explícito
imag_10s = True
imag_20s = True
t = 0

inicio = time.time()
print(inicio)
while True:
    To = T.copy() # salva os valores da matriz T
    for j in range(1, n-1):
        for i in range(1, n-1):
            T[i, j] = To[i, j] + dt*a*(((To[i-1, j] - 2*To[i, j] + To[i+1, j])/dx**2) + ((To[i, j-1] - 2*To[i,j] + To[i, j+1])/dy**2))
            # aplicando as temperaturas no buraco da chapa, pois são constantes
            meio_da_chapa()
    t += dt
    # verifica se chegou nos tempos para salvar o estado atual e depois plotar
    if t >= 10 and imag_10s:
        imag_10s = False
        T10 = T.copy()
    elif t >= 20 and imag_20s:
        imag_20s = False
        T20 = T.copy()
    elif t >= tempo_total:
        T30 = T.copy()
        print(1)
# por ser 3 gráficos decidi salvar como imagem para visualizar todos no final
# preparando plot
X, Y = np.meshgrid(x, y)
# função para facilitar a plotagem
def salvar_grafico(arquivo_nome, matrix, tempo):
    ax = plt.subplot()
    plt.xlabel('Eixo t')
    plt.ylabel('Eixo Y')
    plt.xlim([-0.02, 0.92])
    plt.ylim([-0.02, 0.92])
    plt.title(f'Chapa Plana (2): malha com n={n} e t={tempo}s')
    grafico = ax.contour(X, Y, matrix, 12, vmin=Te, vmax=Tb, linewidths=1, cmap='rainbow') 
    ax.clabel(grafico, fontsize=5, fmt ='%1.1f')
    plt.savefig(f'{arquivo_nome}{tempo}.png', dpi=200)
    ax.clear()


# salvando as imagens
salvar_grafico('chapa_02_t', T10, 10)
salvar_grafico('chapa_02_t', T20, 20)
salvar_grafico('chapa_02_t', T30, 30)
print('tempo: {}  FIM'.format(time.time()-inicio))        