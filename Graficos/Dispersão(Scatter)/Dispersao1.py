

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/Gráfico_de_Dispersão(FG).xlsx') #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabelo de um jeito mais bonito

plt.scatter(tabela['F(gf)'],tabela['l(mm)'],) #Aqui posso criar um gráfico de dispersão com os eixos x e y
plt.xlabel("F(gf)") #Colocando legendas no eixo x
plt.ylabel("l(mm)") #Colocando legendas no eixo y

plt.show()

