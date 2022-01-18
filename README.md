# Excel-Python
Repositório destinado aos estudos da integração entre Python e Excel.

Para isso irei utilizar algumas ferramentas e bibliotecas para análise de dados em python com integração com Excel. 
Vou utilizar a primeiro momento o Pandas para realizar essa integração e o google collab para realizar os códigos em python e integrá-los com os dados do Excel.


# 1º Passo:  Lendo os primeiros dados do Excel no Python

Para isso criei uma simples tabela com dados que irão formar o gráfico da potência de 2, com X e Y, sendo Y a potência de X. 
O Objetivo é ler esses dados utilizando o pandas no Python, a base da dados está abaixo:

<p align="center">
  <img width="300" height="400" src= "https://user-images.githubusercontent.com/62472486/149996438-b37f6eee-9e47-4255-8dc8-0a121d491d51.png">
</p>

Para ler com a base de dados criado no Python, é importante acessá-la utilizando o Pandas. Estou utilizando o google collab, então é importante conectar a base de dados criada no excel a conta do google drive, depois disso é bem tranquilo. Vamos ver o código utilizado abaixo:

   import pandas as pd 
   tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython1.xlsx')
   display(tabela)
   
   O resultado será:
   
<p align="center">
  <img width="300" height="400" src= "https://user-images.githubusercontent.com/62472486/149997437-e453f5b8-17e7-4120-8c34-4187e06c4547.png">
</p>

