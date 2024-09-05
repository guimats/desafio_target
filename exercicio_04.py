'''
4) Dado o valor de faturamento mensal de uma distribuidora,
detalhado por estado:
• SP - R$67.836,43
• RJ - R$36.678,66
• MG - R$29.229,88
• ES - R$27.165,48
• Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de
representação que cada estado teve dentro do valor total mensal da
distribuidora.
'''


# criando função para calcular as porcentagens dos estados
def percentage_calculator(states: dict[str, float]) -> dict[str, float]:
    # novo dict que vai receber os valores das porcentagens e estados
    states_percentage: dict[str, float] = {}
    # somando todos os valores para calcular porcentagem
    sum_values = sum(states.values())
    for key, value in states.items():
        percentage = (round((value * 100) / sum_values, 2))
        states_percentage[key] = percentage
    return states_percentage


states = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
    }

states_percentage = percentage_calculator(states)

# imprimindo valores das porcentagens de cada estado na tela
for key, value in states_percentage.items():
    print(f'{key}: {value}%')
