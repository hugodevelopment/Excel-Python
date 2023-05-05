# Importando nossas bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Lendo nosso arquivo excel
dados = pd.read_excel("Ajuste2.xlsx")
# Aprensentando os dados na tela, no caso o head() apresenta os 5 primeiros itens
dados.head()
# dados = dados[["x","y"]].dropna()
# dados

# Aqui estamos criando um array com os valores de X e igualmente para Y
x = dados["X"].values
y = dados["Y"].values
print(x, y)


#Para calcular M iremos precisar da média de x e y, 
# E criar uma equação para multiplicar os erros de x e y e o erro quadratico de x no denominador

def ajuste(x,y):
  N = len(x)
  x_media = np.mean(x)
  y_media= np.mean(y)
  erro_x = (x - x_media)
  erro_y = (y - y_media)
  erro_quadratico_x = np.sum(erro_x**2)
  m = np.sum((erro_x*erro_y))/erro_quadratico_x
  c = y_media - m*x_media
  # p = np.cov(x,y)[1][0]/np.std(x, ddof =1)*np.std(y,ddof=1)
  r = (np.dot(x, y) - N * x_media * y_media) / ((N - 1) * np.std(x, ddof =1) * np.std(y,ddof=1))
  reta = m * x + c  
  return m,reta,c

def lista():
   for i in ajuste(x,y):
     print(i)

  
def plot_reta(x,y):
    plt.figure(figsize=(12,9))
    m, reta, c = ajuste(x,y)
    plt.scatter(x,y,label="Y(x)");
    plt.grid()
    plt.title(f"y = {m:.3f}x {c:.3f}")
    plt.plot(x,reta,label="Ajuste", color="red")
    plt.xlabel("(T/2pi)²");
    plt.ylabel("L/cos(θ/2)");
    plt.savefig("ajuste2.png")
    plt.legend();
    plt.plot();

print(ajuste(x,y))
plot_reta(x,y)


def incertezas(x,y):
    N = len(x)
    x_media = np.mean(x)
    y_media = np.mean(y)
    sigma_x = np.std(x, ddof=1)
    sigma_y = np.std(y, ddof=1)
    r = (np.dot(x, y) - N * x_media * y_media) / ((N - 1) * np.std(x, ddof =1) * np.std(y,ddof=1))
    e_y =  sigma_y * np.sqrt((N * (1 - r * r)) / (N - 2))
    sigma_a = (1/sigma_x) * (e_y/np.sqrt(N))
    rms = np.sqrt(np.sum(x**2)/N)
    sigma_b = sigma_a * rms
    return (r, e_y, sigma_a , sigma_b)

