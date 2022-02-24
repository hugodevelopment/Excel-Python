from re import X

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython3.xlsx') #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabelo de um jeito mais bonito
#print("O valor do índice 3 na coluna base é:", tabela['Nomes'] [3]) #escolhendo um valor espeficico para ler

plt.hist(tabela["Altura"],rwidth=0.9) #histograma dos dados
# Aqui temos o rwidth que nos mostra o tamanho relativo das barras dos histogramas
plt.title("Altura dos meus parças", fontsize=20)
plt.xlabel("Altura", fontsize=15)
plt.ylabel("Frequência", fontsize=15)
plt.tick_params(labelsize=10)

print()
plt.show()
