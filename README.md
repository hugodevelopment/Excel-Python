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

Agora vamos imprimir um dado especifico em na tabela, neste caso vamos o valor do índice 3. Também aproveitei para melhorar o design dela.

    import pandas as pd 
    tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython1.xlsx') #aqui irá ler os dados em Excel
    display(tabela) #vamos imprimir a tabela de um jeito mais bonito
    print("O valor do índice 3 na coluna base é:", tabela['Base'] [3]) #escolhendo um valor espeficico para ler

O resultado será:

<p align="center">
  <img width="300" height="400" src= "https://user-images.githubusercontent.com/62472486/150399406-c7d89c92-a743-490c-9098-d12e84ed802b.png">
</p>

# 2º Passo:  Gerando os primeiros gráficos do Excel no Python

Para criar os primeiros gráficos de no python com arquivos em Excel é importante duas etapas: 1º Ler a planilha com os dados e 2º utilizar a biblioteca matplotlib.
Após isso, podemos apenas realizar os comandos necessários.

A ideia é reproduzir um gráfico semelhante a este: 

<p align="center">
  <img width="370" height="270" src= "https://user-images.githubusercontent.com/62472486/152660594-3bd40ed3-3dea-444e-a744-10851e9a1fee.png">
</p>

O código utilizando para criar este gráfico de forma semelhante no python foi:

    from re import X
    import pandas as pd
    import matplotlib.pyplot as plt

    tabela = pd.read_excel('/content/drive/MyDrive/Python com Excel/ExcelPython3.xlsx') #aqui irá ler os dados em Excel
    plt.pie(tabela['Idades'],labels= tabela["Nomes"],autopct="%1.0f%%") #gráfico em pizza com legenda e porcentagem
    plt.show()

O resultado foi esse:

<p align="center">
  <img width="300" height="300" src= "https://user-images.githubusercontent.com/62472486/152660722-2bdcc27f-6574-4a13-a37e-deb2d6ebfc83.png">
</p>

Como comparação:

<p align="center">
  <img width="250" height="250" src= "https://user-images.githubusercontent.com/62472486/152699312-6e9ea2c0-ff82-4264-8bec-c0ba48f57e82.png">
</p>









