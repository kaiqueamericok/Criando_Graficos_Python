from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, Series 

wb = Workbook()
ws = wb.active

data = [
    ['Ano', 'Lucro', 'Custos'],
    [2017, 40, 30],
    [2018, 20, 60],
    [2019, 70, 50],
    [2020, 80, 60],
    [2021, 10, 20],
    [2022, 40, 10]
]

for d in data:
    ws.append(d)

# Criação do gráfico
chart = AreaChart()
chart.title = 'Lucro x Custos por Ano'
chart.style = 13
chart.x_axis_title = 'Ano'
chart.y_axis.title = 'Porcentagem'

categorias = Reference(
    ws,
    min_col=1,
    min_row=2,
    max_row=7
)

dados = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_col=3,
    max_row=7
)

chart.add_data(dados, titles_from_data=True)
chart.set_categories(categorias)
ws.add_chart(chart, 'A10')

wb.save('files/chart.xlsx')

