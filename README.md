Gráfico de Lucro x Custos com OpenPyXL
Este projeto gera um gráfico de área comparando Lucros e Custos ao longo dos anos utilizando a biblioteca Python OpenPyXL. Os dados são inseridos em uma planilha Excel e o gráfico é automaticamente criado e salvo no arquivo.

Funcionalidades
Criação de uma planilha Excel com dados de lucro e custos anuais.
Geração de um gráfico de área que compara esses dados de forma visual.
O gráfico possui títulos personalizados e eixos nomeados para fácil interpretação.
Tecnologias Utilizadas
Python 3.x
OpenPyXL: Biblioteca utilizada para manipular planilhas Excel.
Como Rodar o Projeto
Pré-requisitos
Antes de executar o projeto, certifique-se de ter o Python instalado em sua máquina. Você também precisará instalar a biblioteca OpenPyXL, caso ainda não a tenha.

Para instalar o OpenPyXL, execute o comando:

bash
Copiar código
pip install openpyxl
Passo a Passo
Clone este repositório:
bash
Copiar código
git clone https://github.com/seu_usuario/seu_projeto.git
Navegue até o diretório do projeto:
bash
Copiar código
cd seu_projeto
Execute o script Python:
bash
Copiar código
python criar_grafico.py
Resultado
Após a execução do script, um arquivo Excel chamado chart.xlsx será gerado dentro da pasta files. Esse arquivo conterá uma planilha com os dados de lucro e custos por ano, juntamente com um gráfico de área comparando essas informações.

Estrutura do Código
O código está organizado da seguinte forma:

Entrada de Dados: Os dados de anos, lucros e custos são inseridos manualmente em uma lista de listas.
Manipulação da Planilha: Utilizando o Workbook da OpenPyXL, os dados são inseridos na planilha.
Geração de Gráfico: Um gráfico de área é criado a partir dos dados, com títulos e eixos personalizados.
Salvar o Arquivo: O arquivo Excel é salvo no diretório especificado.
Exemplo de Dados Utilizados
Ano	Lucro	Custos
2017	40	30
2018	20	60
2019	70	50
2020	80	60
2021	10	20
2022	40	10
Personalizações Possíveis
Alterar os dados de entrada (anos, lucros e custos).
Modificar o estilo ou tipo de gráfico (área, linha, barras, etc.).
Customizar os títulos e eixos do gráfico.
