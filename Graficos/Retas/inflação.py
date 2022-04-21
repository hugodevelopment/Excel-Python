from re import X

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/Infla2020.xlsx') #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabela de um jeito mais bonito

plt.figure(figsize=(12,6))
plt.plot(tabela['Meses'],tabela['Inflação'])

#Aqui posso criar um gráfico de dispersão com os eixos x e y





