import matplotlib.pyplot as plt
import numpy as np
import time 


# configurando variáveis
tempo_total = 30
Te = 20 # temperatura na extremidade
Ti = 30 # temperatura inicial da chapa
Tb = 100 # temperatura do buraco central
L = 1 # tamanho do lado da chapa
n = 30 # valor de n da malha
a = 0.016
s = 0.1
dx= 2*L/n
dy= dx
dt = s/(a*(1/dx**2 + 1/dy**2))

x = np.linspace(-1, L, n)
y = np.linspace(-1, L, n)
T = Ti * np.ones([n,n])

# iniciar método de euler explícito
imag_10s = True
imag_20s = True
re = L # raio da chapa
ri = L*0.4 # raio do buraco

t = 0
inicio = time.time()
while True:
    To = T.copy() # salva os valores da matriz T
    for j in range(1, n-1):
        for i in range(1, n-1):
            # aplicando as temperaturas no buraco da chapa, pois são constantes
            r = np.sqrt(y[i]**2  + x[j]**2)
            if r < re and r > ri:
                T[i, j] = To[i, j] + dt*a*(((To[i-1, j] - 2*To[i, j] + To[i+1, j])/dx**2) + ((To[i, j-1] - 2*To[i,j] + To[i, j+1])/dy**2))
            if r >= re:
                T[i, j] = Ti
            if r <= ri:
                T[i, j] = Tb

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
        # saindo do loop pois t já chegou em 30s
        break

# por ser 3 gráficos decidi salvar como imagem para visualizar todos no final
# preparando plot
X, Y = np.meshgrid(x, y)
# função para facilitar a plotagem
def salvar_grafico(arquivo_nome, matrix, tempo):
    ax = plt.subplot()
    plt.xlabel('Eixo t')
    plt.ylabel('Eixo Y')
    plt.xlim([-1.02, 1.02])
    plt.ylim([-1.02, 1.02])
    plt.title(f'Chapa Plana (3): malha com n={n} e t={tempo}s')
    grafico = ax.contour(X, Y, matrix, 9, vmin=Te, vmax=Tb, linewidths=1, cmap='rainbow') 
    ax.clabel(grafico, fontsize=5, fmt ='%1.1f')
    plt.savefig(f'{arquivo_nome}{tempo}.png', dpi=200)
    ax.clear()


# salvando as imagens
salvar_grafico('chapa_03_t', T10, 10)
salvar_grafico('chapa_03_t', T20, 20)
salvar_grafico('chapa_03_t', T30, 30)
print('tempo: {}  FIM'.format(time.time()-inicio))        