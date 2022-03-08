from re import X

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import mean
from numpy import std

#Agora irei estudar como colocar e editar legendas no gráfico para ficar mais bonito e visual

#Neste caso irei plotar a função f(x) = 2x
tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython5.xlsx') #aqui irá ler os dados em Excel
display(tabela)

plt.figure(figsize=(6,4))
plt.plot(tabela["x"], tabela["y"])

# Agora irei inserir as legendas nos eixos x e y
plt.xlabel("x")
plt.ylabel("f(x) = y")
plt.grid(True) #Aqui coloco uma linhas de grade

# Vou adicionar uma nova linha no gráfico
plt.plot(tabela['x/2'])






