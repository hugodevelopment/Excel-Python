from re import X

import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython4.xlsx') #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabelo de um jeito mais bonito
#print("O valor do índice 3 na coluna base é:", tabela['Base'] [3]) #escolhendo um valor espeficico para ler

#plt.plot(tabela["Altura"]) #histograma dos dados
#plt.plot(tabela['Idades']) #gráfico de linha da altura
#plt.pie(tabela['Idades'],labels= tabela["Nomes"],autopct="%1.0f%%") #gráfico em pizza com legenda e porcentagem

plt.scatter(tabela['F(gf)'],tabela['l(mm)'],) #Aqui posso criar um gráfico de dispersão
plt.xlabel("F(gf)") #Colocando legendas no eixo x
plt.ylabel("l(mm)") #Colocando legendas no eixo y
plt.show()

