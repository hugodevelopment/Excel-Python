import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tabela = pd.read_excel('PlanilhaMec.xlsx') #aqui irá ler os dados em Excel
#display(tabela) #vamos imprimir a tabelo de um jeito mais bonito


# Criando o histograma para os dados da largura, com o int
plt.hist(tabela['Largura(cm)'], bins= 4, edgecolor="black")

# Colocando o título no histograma
plt.title("Histograma Largura (cm)")

média = 149.5
cor = "#FA8072"
plt.axvline(média, color=cor, label="Média_Largura: 149,5")
plt.legend()

plt.grid()

# Colocando legenda nos Eixos
plt.xlabel("Largura (cm)")
plt.ylabel("Frequência dos dados")

plt.tight_layout()
 

plt.show()

