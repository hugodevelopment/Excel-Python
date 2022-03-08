from re import X

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import mean
from numpy import std

#Agora irei estudar como colocar e editar legendas no gráfico para ficar mais bonito e visual

# Neste caso irei plotar a função f(x) = 2x
tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython5.xlsx') #aqui irá ler os dados em Excel
display (tabela)

plt.figure(figsize=(6,4))
plt.plot(tabela["x"], tabela["y"])



