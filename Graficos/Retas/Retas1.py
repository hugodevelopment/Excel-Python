from re import X

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython4.xlsx') #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabelo de um jeito mais bonito

#Aqui posso criar um gráfico de dispersão com os eixos x e y
plt.scatter(tabela['F(gf)'],tabela['l(mm)'], color="red", label="Medias: F(gf) 11.7 e l(mm) 35.09") 
plt.xlabel("F(gf)") #Colocando legendas no eixo x
plt.ylabel("l(mm)") #Colocando legendas no eixo y
plt.grid(True)
plt.legend()
plt.show()

print()
print("Media de F(gf): ", str(round(mean(tabela['F(gf)']),2)))
print("Media de l(mm): ", str(round(mean(tabela['l(mm)']),2)))

print("Desvio Padrão de F(gf)", str(round(std(tabela['F(gf)']),1)))
print("Desvio Padrão de l(mm)", str(round(std(tabela["l(mm)"]),1)))












