{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "CalculosMecanica.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "!pip install nbconvert"
      ],
      "metadata": {
        "id": "7Z_cx-RY1I79"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Para começar a coletar os dados vamos realizar os seguintes cálculos:**\n",
        "\n",
        "1.   Média de C, L e A\n",
        "2.   Desvio Padrão de C, L e A\n",
        "3.   Erro da Média de C, L A\n",
        "4.   Erro Padrão de C e L\n",
        "\n",
        "**O erro da média é calculado pela seguinte relação:**\n",
        "\n",
        "\\begin{equation}\n",
        " \\boxed{σ_{\\overline{x}} = \\frac{\\sigma_{x}}{\\sqrt{N}}} \n",
        "\\end{equation}\n",
        "\n",
        "**O erro da padrão é calculado pela seguinte relação:**\n",
        "\n",
        "\\begin{equation}\n",
        " \\boxed{\\sigma = \\sqrt{\\sigma_A^2 + \\sigma_B^2}} \n",
        "\\end{equation}"
      ],
      "metadata": {
        "id": "bp1qfnuVZcwG"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "cLsnLMYodZ2S",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "6d356cb1-31b9-47e6-f9bd-15364d415ad8"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "    Mesa      C     L      Área Área Mesas da Turma\n",
              "0      1  149.0  75.0  11175.00             11269.4\n",
              "1      2  150.0  75.0  11250.00             11256.4\n",
              "2      3  147.0  75.0  11025.00             11268.3\n",
              "3      4  150.0  75.0  11250.00            11263.79\n",
              "4      5  149.0  75.0  11175.00             11265.5\n",
              "5      6  149.0  75.0  11175.00            11278.52\n",
              "6      7  149.5  75.0  11212.50            11279.71\n",
              "7      8  149.6  74.9  11205.04             11264.4\n",
              "8      9  149.7  74.8  11197.56            11272.48\n",
              "9     10  149.0  74.8  11145.20            11290.83\n",
              "10    11  150.0  75.0  11250.00            11203.23\n",
              "11    12  150.0  74.5  11175.00             11267.7\n",
              "12    13  149.0  75.0  11175.00           11,305,25\n",
              "13    14  150.0  74.7  11205.00            11280.28\n",
              "14    15  149.0  74.9  11160.10                 NaN\n",
              "15    16  149.6  75.0  11220.00                 NaN\n",
              "16    17  149.8  75.0  11235.00                 NaN\n",
              "17    18  149.8  75.0  11235.00                 NaN\n",
              "18    19  149.8  75.0  11235.00                 NaN\n",
              "19    20  149.7  75.0  11227.50                 NaN\n",
              "20    21  149.7  75.0  11227.50                 NaN\n",
              "21    22  149.8  74.8  11205.04                 NaN\n",
              "22    23  149.8  75.0  11235.00                 NaN\n",
              "23    24  150.0  75.0  11250.00                 NaN\n",
              "24    25  149.8  75.0  11235.00                 NaN"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-56f890d3-a3ae-47ec-9314-afdbaeb4abee\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Mesa</th>\n",
              "      <th>C</th>\n",
              "      <th>L</th>\n",
              "      <th>Área</th>\n",
              "      <th>Área Mesas da Turma</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>149.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11175.00</td>\n",
              "      <td>11269.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>150.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11250.00</td>\n",
              "      <td>11256.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>147.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11025.00</td>\n",
              "      <td>11268.3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>150.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11250.00</td>\n",
              "      <td>11263.79</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>149.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11175.00</td>\n",
              "      <td>11265.5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>6</td>\n",
              "      <td>149.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11175.00</td>\n",
              "      <td>11278.52</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>7</td>\n",
              "      <td>149.5</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11212.50</td>\n",
              "      <td>11279.71</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>8</td>\n",
              "      <td>149.6</td>\n",
              "      <td>74.9</td>\n",
              "      <td>11205.04</td>\n",
              "      <td>11264.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>9</td>\n",
              "      <td>149.7</td>\n",
              "      <td>74.8</td>\n",
              "      <td>11197.56</td>\n",
              "      <td>11272.48</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>10</td>\n",
              "      <td>149.0</td>\n",
              "      <td>74.8</td>\n",
              "      <td>11145.20</td>\n",
              "      <td>11290.83</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>11</td>\n",
              "      <td>150.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11250.00</td>\n",
              "      <td>11203.23</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>12</td>\n",
              "      <td>150.0</td>\n",
              "      <td>74.5</td>\n",
              "      <td>11175.00</td>\n",
              "      <td>11267.7</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>13</td>\n",
              "      <td>149.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11175.00</td>\n",
              "      <td>11,305,25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>14</td>\n",
              "      <td>150.0</td>\n",
              "      <td>74.7</td>\n",
              "      <td>11205.00</td>\n",
              "      <td>11280.28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>15</td>\n",
              "      <td>149.0</td>\n",
              "      <td>74.9</td>\n",
              "      <td>11160.10</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>16</td>\n",
              "      <td>149.6</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11220.00</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>17</td>\n",
              "      <td>149.8</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11235.00</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>18</td>\n",
              "      <td>149.8</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11235.00</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>19</td>\n",
              "      <td>149.8</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11235.00</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>20</td>\n",
              "      <td>149.7</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11227.50</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>21</td>\n",
              "      <td>149.7</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11227.50</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>22</td>\n",
              "      <td>149.8</td>\n",
              "      <td>74.8</td>\n",
              "      <td>11205.04</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>23</td>\n",
              "      <td>149.8</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11235.00</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>24</td>\n",
              "      <td>150.0</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11250.00</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>25</td>\n",
              "      <td>149.8</td>\n",
              "      <td>75.0</td>\n",
              "      <td>11235.00</td>\n",
              "      <td>NaN</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-56f890d3-a3ae-47ec-9314-afdbaeb4abee')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-56f890d3-a3ae-47ec-9314-afdbaeb4abee button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-56f890d3-a3ae-47ec-9314-afdbaeb4abee');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "---------------- Calculos da Média ------------------------------\n",
            "Media do Comprimento(cm):  149.5\n",
            "Media do Largura(cm):  74.94\n",
            "Media da Área(cm²):  11203.22\n",
            "\n",
            "---------------- Calculos do Desvio Padrão Amostral -----------------\n",
            "Desvio Padrão da Comprimento(cm):  0.63\n",
            "Desvio Padrão da Largura(cm):  0.12\n",
            "Desvio Padrão da Área(cm²):  47.48\n",
            "\n",
            "---------------- Calculos Erro da Média -----------------\n",
            "Erro médio do Comprimento(cm):  0.13\n",
            "Erro médio da Largura(cm):  0.02\n",
            "Erro médio da Área (cm²):  9.5\n",
            "\n",
            "-------- Calculos Erro Padrão Largura e Comprimento --------\n",
            "Erro Padrão Comprimento:  0.638\n",
            "Erro Padrão Largura:  0.16\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "from numpy import mean\n",
        "from numpy import std\n",
        "\n",
        "tabela = pd.read_excel(\"/content/PlanilhaMec.xlsx\") #aqui irá ler os dados em Excel\n",
        "display(tabela) #vamos imprimir a tabela de um jeito mais bonito\n",
        "\n",
        "print()\n",
        "\n",
        "print('---------------- Calculos da Média ------------------------------')\n",
        "\n",
        "print(\"Media do Comprimento(cm): \", str(round(mean(tabela['C']),2)))\n",
        "print(\"Media do Largura(cm): \", str(round(mean(tabela['L']),2)))\n",
        "print(\"Media da Área(cm²): \", str(round(mean(tabela['Área']),2)))\n",
        "\n",
        "print()\n",
        "\n",
        "print('---------------- Calculos do Desvio Padrão Amostral -----------------')\n",
        "\n",
        "print(\"Desvio Padrão da Comprimento(cm): \", str(round(std(tabela['C']),2)))\n",
        "print(\"Desvio Padrão da Largura(cm): \", str(round(std(tabela['L']),2)))\n",
        "print(\"Desvio Padrão da Área(cm²): \", str(round(std(tabela['Área']),2)))\n",
        "\n",
        "print()\n",
        "\n",
        "print('---------------- Calculos Erro da Média -----------------')\n",
        "\n",
        "Raiz_das_medidas = 5\n",
        "\n",
        "\n",
        "Dp_Comprimento = np.std(tabela[\"C\"])\n",
        "Erro_Media_Comprimento = Dp_Comprimento / Raiz_das_medidas\n",
        "print(\"Erro médio do Comprimento(cm): \", round(Erro_Media_Comprimento,2))\n",
        "\n",
        "Dp_Largura = np.std(tabela[\"L\"])\n",
        "Erro_Media_Largura = Dp_Largura / Raiz_das_medidas\n",
        "print(\"Erro médio da Largura(cm): \", round(Erro_Media_Largura,2))\n",
        "\n",
        "\n",
        "Dp_Area = np.std(tabela[\"Área\"])\n",
        "Erro_Media_Área = Dp_Area / Raiz_das_medidas\n",
        "print(\"Erro médio da Área (cm²): \",round(Erro_Media_Área,2))\n",
        "\n",
        "print()\n",
        "\n",
        "print('-------- Calculos Erro Padrão Largura e Comprimento --------')\n",
        "\n",
        "Erro_do_instrumento = 0.1\n",
        "\n",
        "Erro_total_comprimento = np.sqrt((Erro_do_instrumento)**2 + (Dp_Comprimento)**2)\n",
        "print(\"Erro Padrão Comprimento: \",round(Erro_total_comprimento,3))\n",
        "\n",
        "Erro_total_largura = np.sqrt(((Erro_do_instrumento)**2 + (Dp_Largura)**2))\n",
        "print(\"Erro Padrão Largura: \", round(Erro_total_largura,2))\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Histogramas que precisamos:\n",
        "\n",
        "*   Histograma da Largura (cm)\n",
        "*   Histograma do Comprimento (cm)\n",
        "*   Histograma da Área (cm²)\n",
        "\n"
      ],
      "metadata": {
        "id": "zuLuBlUatm0D"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import matplotlib.pyplot as plt\n",
        "tabela = pd.read_excel(\"/content/PlanilhaMec.xlsx\") #aqui irá ler os dados em Excel\n",
        "\n",
        "bin_count = int(np.ceil(np.log2(len(tabela['L']))) + 1)\n",
        "\n",
        "# Criando o histograma para os dados da largura, com o int\n",
        "plt.hist(tabela['L'], bins= bin_count, edgecolor=\"black\")\n",
        "\n",
        "# Colocando o título no histograma\n",
        "plt.title(\"Histograma Largura (cm)\")\n",
        "\n",
        "\n",
        "\n",
        "#Podemos criar um legenda no gráfico para apontar a média\n",
        "média = 74.9\n",
        "cor = \"#FA8072\"\n",
        "plt.axvline(média, color=cor, label=\"Média_Largura: 74,9\")\n",
        "plt.legend()\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "# Colocando legenda nos Eixos\n",
        "plt.xlabel(\"Largura (cm)\")\n",
        "plt.ylabel(\"Frequência dos dados\")\n",
        "\n",
        "plt.tight_layout()\n",
        "#plotando o gráfico\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "AciDbNmAh_Og",
        "outputId": "7fcd6889-946b-4a23-ca49-96f53f89de9d"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "tabela = pd.read_excel(\"/content/PlanilhaMec.xlsx\") #aqui irá ler os dados em Excel\n",
        "# Criando o histograma para os dados da Área\n",
        "plt.hist(tabela['Área'],bins=bin_count, edgecolor=\"black\")\n",
        "\n",
        "# Colocando o título no histograma\n",
        "plt.title(\"Histograma Area (cm²)\")\n",
        "\n",
        "#Podemos criar um legenda no gráfico para apontar a média\n",
        "média = 11203.23\n",
        "cor = \"#FA8072\"\n",
        "plt.axvline(média, color=cor, label=\"Média_Área: 11203.23\")\n",
        "plt.legend()\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "# Colocando legenda nos Eixos\n",
        "plt.xlabel(\"Área (cm²)\")\n",
        "plt.ylabel(\"Frequência dos dados\")\n",
        "\n",
        "plt.tight_layout()\n",
        " \n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "outputId": "11236a0c-58a4-4088-f385-29c6f80d94f4",
        "id": "LcrV62WJVOzt"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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HlRz1q5dS11dHatWrSp3KO2yzTbbsGDBgnKH0WGUor169OhBZWUlW2yxRVHrNbP26bAJqq6ujq233poBAwYgtfVh0uW3YsUKtt666SwG1pJit1dEsHz5curq6thtt92KVq+ZtV+HvcS3atUq+vTp06GTk5WfJPr06dPhe+JmnVGHTVCAk5MVhc8js2zq0AnKzMw6LycoMzPLJCeoTubKK69k6tSp5Q7DrMvrV7kLkjr1a+7ceSVtww47iq+jufnmmznhhBPo3bt3yfbx4YcfMnDgQE4++eSS7cPM8rPstaXseun95Q6jpNauXVjS+t2DagdJnHrqqY3L69ato2/fvhxxxBHrbXfNNdfQu3fvFpNTdXV147MGDz/8cN599902xTNv3jzOOOMMHn54YzOHF8/MmTMZOXIk3bp14+67715v3bhx49h22203aItTTjmFPfbYgyFDhnDWWWexdu1aIBnufeGFFzJo0CCGDRvGc889B8CSJUsYOXIkI0aMYPDgwfzsZz9rNpZLLrmEPffck2HDhjF+/PjGNpw1axYjRoxgxIgRDB8+nHvvvbfYzWBmJeIE1Q5bbbUV8+fPZ+XKlQA89thj7Lzzzhts9+1vf5sTTjghrzoffPBBtt122zbFM3XqVPbff/8WL/FFBB999FGb6m7OLrvswuTJk/niF7+4wbpLLrmEKVOmbFB+yimnsHDhQubNm8fKlSu59dZbAXjooYdYtGgRixYt4pZbbuHcc88FoF+/fjz11FPMmTOHZ555hu9///u8/vrrG9R7yCGHMH/+fObOncunP/1pvvOd7wAwZMgQZs+ezZw5c3j44Yc555xzWLduXdHawMxKp1Nc4vvw4d8Syzb8pdUe2nEnNh93TKvbHX744TzwwAMcd9xxTJ06lZNPPpknnngCSB5Ff8EFFzB//nzWrl3LVVddxdFHH83KlSs588wzeeGFFxg0aFBjgoOPn9y+/fbbc8wxx7B06VJWrVrFRRddxIQJE1qMIyK46667eOyxxzjggANYtWoVPXr0YPHixRx66KGMHj2a2tpaHnzwQe68807uvPNOVq9ezfjx47n66qsBCtpfQ6wAm2224d85Bx98MDU1Nc22V4PPfvaz1NXVAXDfffdx2mmnIYkxY8bw7rvv8sYbb9CvX7/G7VevXt1igv3CF77Q+H7MmDGNPbqePXs2lq9atcpDys06EPeg2umkk05i2rRprFq1irlz5zJ69OjGdZMmTeKggw5i1qxZ/OEPf+CSSy7hgw8+4KabbqJnz54sWLCAb3zjG9TW1jZb92233UZtbS2zZ8/mhhtuYPny5S3G8ec//5nddtuNT33qU1RXV/PAAw80rlu0aBHnnXceL774Ii+//DKLFi1i1qxZzJkzh9raWmbOnLnR/Z199tlFn+5k7dq1TJkyhXHjxgHw2muv0b9//8b1lZWVvPbaawAsXbqUYcOG0b9/f772ta+x0047bbTu2267jcMOO6xx+ZlnnmHw4MEMHTqUn/zkJ3Tr1in+LjPr9DrF/9R8ejqlMmzYMBYvXszUqVPX6x0APProo0yfPp3rrrsOSP6C/9vf/sbMmTO58MILgeQS1LBhw5qt+4Ybbmi8Z7J06VIWLVpEnz59mt126tSpnHTSSUCSNG+//XaOPfZYAHbddVfGjBnTGNOjjz7KZz7zGQDq6+tZtGgRBx54YIv7a7gMV0znnXceBx54IAcccECr2/bv35+5c+fy+uuvc+SRR3LqqadSUVHR7LaTJk2iW7dunHLKKY1lo0eP5sUXX2TBggWcfvrpHHbYYfTo0aNox2JmpdEpElS5HXXUUVx88cXU1NSs18uJCO655x722GOPguusqanh8ccf56mnnqJnz55UV1e3+DieDz/8kHvuuYf77ruPSZMmNT5fbsWKFQDrzxAaweWXX84555zT5v2119VXX83bb7/NzTff3Fi28847s3Tp0sblurq6De7n7bTTTuy999488cQTHHfccRvUO3nyZO6//35mzJjR7KW8vfbai169ejF//nyqqqqKeERmVgq+xFcEZ511FldeeSVDhw5dr/zQQw/lRz/6EREBwPPPPw/AgQceyK9+9SsAXnrpJebOnbtBne+99x69e/emZ8+eLFy4kKeffrrF/c+YMYNhw4axdOlSFi9ezJIlSzj22GObHbF26KGHctttt1FfXw8kl9beeuutgvbXHrfeeiuPPPIIU6dOXe/e1VFHHcXtt99ORPD000+zzTbb0K9fP+rq6hrv0b3zzjs89dRTzSb8hx9+mO9+97tMnz59vftOr776auOgiCVLlrBw4cLGe2dmlm1OUEVQWVnZeMku1xVXXMHatWsZNmwYgwcP5oorrgDg3HPPpb6+nr322otJkyYxatSoDT47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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "tabela = pd.read_excel(\"/content/PlanilhaMec.xlsx\") #aqui irá ler os dados em Excel\n",
        "# Criando o histograma para os dados da Área\n",
        "plt.hist(tabela['C'],bins=4, edgecolor=\"black\")\n",
        "\n",
        "# Colocando o título no histograma\n",
        "plt.title(\"Histograma Comprimento(cm)\")\n",
        "\n",
        "#Podemos criar um legenda no gráfico para apontar a média\n",
        "média =  149.5\n",
        "cor = \"#FA8072\"\n",
        "plt.axvline(média, color=cor, label=\"Média_Comprimento:  149.5\") \n",
        "plt.legend()\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "# Colocando legenda nos Eixos\n",
        "plt.xlabel(\"Comprimento(cm)\")\n",
        "plt.ylabel(\"Frequência dos dados\")\n",
        "\n",
        "plt.tight_layout()\n",
        " \n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 297
        },
        "id": "V7CDWyV4uOKr",
        "outputId": "77cc32d5-c339-4a91-cca4-dbeac47b0ba2"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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PXs2c+bMYcWKFYwcOZKDDz6YAQMGMHz48Lpym6qmpoZrrrmGWbNmbXR5b5999uE73/kOK1eupGfPnjz00EOUlWX//+rpp59mv/32Y/vtt+e6665j77333qxYzIpRXhNURDwhaXC2bUrGz54MfD6fMWTKpaezJk9f9tx3331ZvHgxt99+O2PHjt1o28MPP8z9999f90du7dq1LF26lCeeeIL/+q//qtt/3333zVr3T37yE+69914AXn/9dV5++eWsCaoxTz31FCeccEJdT+DEE0/kySefZNy4cQwZMoRhw4YBsPfee3PooYciiWHDhrF48eK6Oo477jh69uxJz549qaio4LnnnmOrrbZi1KhRWZMTwMiRIxkwYAAAu+yyC4cffjgAw4YN47HHHgPgkUce2egy5OrVq6mpqQHg6KOPpnv37nTv3p3+/fuzfPnyrG2bMGECnTt3prS0lEMOOYS//e1vjBs3brOTE8CUKVO44IILKCkp2Wj9nnvuycUXX8zhhx9O7969G/ynYP/992fJkiWUlJTw0EMPcfzxx/Pyyy9vdjxmxaYtP4P6HLA8Ihp6RwbwsKQAbo6I6a0XWn6MGzeOiy66iMrKSlauXFm3PiK4++672WOPPRrZO7vKykoeeeQRnn76aXr16kV5eXmDX+wcOnQoc+bMYcOGDVn/YDake/fudc87depUt9ypUyfWr19ft63+d3Zqlxu7V0wudX/88cc888wz9OjRo9H9O3fuvFE8+fbss89y1113MXnyZFatWkWnTp3o0aMH5557LmeeeSZnnnkmAJdeemnW6Yq22GKLuudjx47lG9/4BitWrKBfv36t1gazQtaWCWoCcHsj28dExBuStgVmSVoYEU/ULyRpIjARoLS0lMrKyo22b7nlllRXV+cc1IYNGzapfK6qq6s5+eST6dGjB4MHD+b1119n/fr1VFdXU1FRwdSpU7nuuuuQxJw5c9hvv/0YPXo0t912GyNHjuSll15i7ty5vP/++1RXVxMR1NTU8Pbbb9OnTx82bNhAVVUVzzzzDB988EHWNuy0004MHz6cSy65hMsvvxxJLFmyhAULFrD//vvz9a9/nW9+85t1CXP69OnU1NTw8ccf19W3bt061qxZQ3V19UbbPvzwQx588EHOPfdc3n//fR577DEuu+wyFi1aVNfO+q/HBx98sNG2DRs21LUvc1tFRQXXXXcd5513HpBcStx333358MMP6dq1a93+ta9JSUkJq1evrltfVlbGjBkzOPHEE3nvvfd4/PHHufLKKzf5PGfGBxsPVPnBD35ASUkJX/3qV6murubdd9+lf//+vP7669x11108+uijnzre8uXL2XbbbZHE888/z4YNG+jWrdunyq1du7buM7ti1drtu+666+i2Xf7/mRm0LOjaGS4c1nr/OLW2bbsMzNu5a5MEJakLcCJwQENlIuKN9Oc7ku4FRgGfSlBpz2o6QFlZWdS/cdaCBQs26ZJdvuZz69OnD0OHDmXo0KEA9OrViy5dutCnTx+++93vcv7553PQQQfx8ccfM2TIEB544AHOP/98Tj/9dEaNGsWee+7JAQccQO/evenTpw+SKCkp4YQTTuC2225j1KhR7LHHHhx44IH06tUraxuqq6u59dZbufDCCxkxYgQ9e/akX79+XHvttYwcOZIzzjiDQw89FICJEycyZswYFi9eTKdOnerq69q1Kz179qRPnz6UlJTUbevevTvDhw9n3LhxrFixgiuuuILdd9+dN998s66d9V+PzNcAkh5Qbfsyt910001885vf5KCDDmL9+vUcfPDBTJs2re7SXu3+ta/J4MGDGTNmDJ/5zGc46qij+OEPf8js2bMZM2YMkrj22mvrRtTl8hnUvffey6RJk3j33Xc5+eSTGT58OH/+8583KlM/lrFjx7Jy5Uq6du3KTTfdxKBBgwCYNm0aAOeccw633XYbN910E126dKFnz57ccccdG/WqavXo0YOSkpKivKFfrda+YWFFRUWrjKwb0U0M6h1MnVe8A6Yn9V+2SYOONoUiIi8V1x0g+QzqgdpRfOm6I4FvR8QhDezTG+gUEdXp81nAVRHxp8aOVVZWFvW/p7JgwYJGR2HVV2wTjmbKZ9umTJlCSUkJF110UV7qz0WxnrsFCxawfPlyJ6gWJKlVEtSvu73AoN7BIe81+L94uzep/0IuvPDCZtUhqSrbSO28flFX0u3A08AekpZJOjPddAr1Lu9J2l5S7TWTUuApSXOA54AHm0pOZmZWXPI9im9CA+tPy7LuTWBs+vxVYL98xlbsRo8ezYcffrjRumnTpnHggQfm5XhTpkzJS71m1nEV74XRDi7b9EX5GPxhZpYvHWIuvnx/zmaWL/7dtY6s6BNUjx49WLlypd/o1u7U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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Calculando a correlação entre dos dados do comprimento e largura.\n",
        "\n",
        "**Para isso iremos utilizar a covariancia entre x e y e coeficiente de Pearson (r). Depois iremos criar o gráfico de dispersão para visualizar como as grandezas de correlacionam graficamente.**\n",
        "\n",
        "**Coeficiente de correlação linear de Pearson(r) que varia o intervalo entre -1 e 1.**\n",
        "\n",
        "\n",
        "\\begin{equation}\n",
        " \\boxed{r = \\frac{\\sigma_{xy}}{\\sigma_{x}\\sigma_{y}}} \n",
        "\\end{equation}\n",
        "\n",
        "Pela só precisamos calcular a covariancia e dividir pelo produto dos desvios padraões\n"
      ],
      "metadata": {
        "id": "AmOzSWxewW23"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "\n",
        "\n",
        "print(\"Calculando a covariancia entre comprimento e largura\")\n",
        "Covariancia = np.cov(tabela[\"C\"], tabela[\"L\"])[1][0]\n",
        "\n",
        "print()\n",
        "\n",
        "print(\"Covariancia entre Comprimento e Largura:\", Covariancia)\n",
        "\n",
        "print()\n",
        "\n",
        "print(\"Calculando o Coeficiente de Pearson\")\n",
        "\n",
        "print()\n",
        "\n",
        "r = Covariancia/(Dp_Comprimento*Dp_Largura)\n",
        "\n",
        "print(\"Coeficiente de Pearson (r) =\", r)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UfMn9Mesw5tm",
        "outputId": "f1ca0a7f-86d0-4607-cbfc-e39b03e754d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Calculando a covariancia entre comprimento e largura\n",
            "\n",
            "Covariancia entre Comprimento e Largura: -0.01473333333333329\n",
            "\n",
            "Calculando o Coeficiente de Pearson\n",
            "\n",
            "Coeficiente de Pearson (r) = -0.19022130357241276\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Podemos ver que tanto a covariancia, quanto o coeficente de Pearson deram valores negativos, logo as grandezas de comprimento e largura não são correlacionadas entre si, na verdade são inversamente correlacionadas. \n",
        "Quando uma cresce, outra cai e vice-versa. Podemos avaliar isso pelo gráfica de dispersão abaixo.**"
      ],
      "metadata": {
        "id": "ZUf6A3uh-yAX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "tabela = pd.read_excel(\"/content/PlanilhaMec.xlsx\")#aqui irá ler os dados em Excel\n",
        "\n",
        "plt.scatter(tabela[\"C\"],tabela[\"L\"],) #Aqui posso criar um gráfico de dispersão com os eixos x e y\n",
        "plt.xlabel(\"Comprimento(cm)\") #Colocando legendas no eixo x que é o comprimento neste caso\n",
        "plt.ylabel(\"Largura(cm)\") #Colocando legendas no eixo y que é a largura neste caso\n",
        "\n",
        "plt.title(\"Dispersão entre C(cm) x L(cm)\")\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 295
        },
        "id": "bFJGJdqj2w9c",
        "outputId": "d8d919cc-2ec4-4d6c-e49f-da4aaea7d944"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "tabela = pd.read_excel(\"/content/drive/MyDrive/Colab Notebooks/PlanilhaMec.xlsx\")#aqui irá ler os dados em Excel\n",
        "\n",
        "plt.scatter(tabela[\"L\"],tabela[\"C\"],) #Aqui posso criar um gráfico de dispersão com os eixos x e y\n",
        "plt.xlabel(\"Largura(cm)\") #Colocando legendas no eixo x que é o comprimento neste caso\n",
        "plt.ylabel(\"Comprimento(cm)\") #Colocando legendas no eixo y que é a largura neste caso\n",
        "\n",
        "plt.grid()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 279
        },
        "id": "i_A9JcQuN42e",
        "outputId": "80d971c4-dba1-4fbd-967e-8e63d35b9228"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Podemos ver também que os gráficos não apresentam correlação, o maior valor de uma grandeza é o menor de outra**"
      ],
      "metadata": {
        "id": "DVxgy49ROHD_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        ""
      ],
      "metadata": {
        "id": "HEOslBN6PN2b"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "**Agora podemos calcular a incerteza da Área por meio da propagação de erros utilizando a relação abaixo:**\n",
        "\n",
        "\\begin{equation}\n",
        " \\boxed{σ_{A} = A \\sqrt{\\left (\\dfrac{σ_{c}}{c} \\right)^2 + \\left (\\dfrac{ σ_{l}}{l} \\right)^2}} \n",
        "\\end{equation}"
      ],
      "metadata": {
        "id": "vscYsMzeAVpR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Calculando as medias de C, L e A\n",
        "\n",
        "# Média do Comprimento\n",
        "Media_C = np.mean(tabela[\"C\"])\n",
        "print(\"Média de Comprimento: \", round(Media_C,2))\n",
        "\n",
        "#Média da Largura\n",
        "Media_L = np.mean(tabela[\"L\"])\n",
        "print(\"Média da largura: \", round(Media_L,2))\n",
        "\n",
        "# A média sendo Média de C * Média de L\n",
        "A_Media = Media_C * Media_L\n",
        "\n",
        "print(\"Média da Área: \", round(A_Media,2))\n",
        "\n",
        "#Calculando a propagação de erros\n",
        "Propagação = A_Media * np.sqrt((Erro_Media_Comprimento/Media_C)**2 + (Erro_Media_Largura/Media_L)**2)\n",
        "print(\"Incerteza Área: \", round(Propagação,2))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EfrUT6dy_FvD",
        "outputId": "50f19d5d-eb46-406d-ea65-3ab1a3eeb675"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Média de Comprimento:  149.5\n",
            "Média da largura:  74.94\n",
            "Média da Área:  11203.23\n",
            "Incerteza Área:  10.13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "!jupyter nbconvert --to html CalculosMecanica.ipynb\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "81459341-8850-49e1-a507-b8fc0e2cf46b",
        "id": "V1GcjNfB3QcY"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[NbConvertApp] Converting notebook CalculosMecanica.ipynb to html\n",
            "[NbConvertApp] Writing 389664 bytes to CalculosMecanica.html\n"
          ]
        }
      ]
    }
  ]
}