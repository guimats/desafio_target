'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à
média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados.
Estes dias devem ser ignorados no cálculo da média;
'''
import json
import os

# pegando o caminho do arquivo json
FILE_NAME = 'dados.json'
FILE_ABSOLUTE_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        FILE_NAME
    )
)


# criando função para separar valores de cada dia em uma lista
def invoicing_values(file) -> list[float]:
    values = []
    for data in file:
        for key, value in data.items():
            if key == 'valor':
                values.append(value)
    return values


# checando a lista de valores e retornando o menor e maior valor (exceto zero)
def lowest_and_highest_value(file) -> tuple[float, float]:
    values = invoicing_values(file)
    min_value = min(filter(lambda a: a != 0, values), key=int)
    max_value = max(values, key=int)
    return min_value, max_value


# fazendo média dos valores e retornando a quantidade de dias acima da média
def above_average_days(file) -> int:
    values = invoicing_values(file)
    average = sum(values) / len(values)
    days = []
    for i, _ in enumerate(values):
        if values[i] > average:
            days.append(i+1)
    return len(days)


# abrindo arquivo JSON e executando as funções
with open(FILE_ABSOLUTE_PATH, 'r') as file:
    daily_invoicing = json.load(file)
    min_value, max_value = lowest_and_highest_value(daily_invoicing)
    days = above_average_days(daily_invoicing)
    print(f'Menor valor: {min_value}\nMaior valor: {max_value}\n'
          f'Dias acima da média: {days}')
