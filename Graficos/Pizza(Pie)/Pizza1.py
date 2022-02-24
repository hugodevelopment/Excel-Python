from re import X

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from numpy import mean
from numpy import std

tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython3.xlsx') #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabelo de um jeito mais bonito
#plt.pie(tabela['Idades'],labels= tabela["Nomes"],autopct="%1.0f%%") #gráfico em pizza com legenda e porcentagem
plt.show()

