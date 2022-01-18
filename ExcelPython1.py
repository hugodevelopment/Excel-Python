import pandas as pd 

tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython1.xlsx') #aqui irá ler os dados em Excel
display(tabela) #vamos imprimir a tabelo de um jeito mais bonito
print("O valor do índice 3 na coluna base é:", tabela['Base'] [3]) #escolhendo um valor espeficico para ler