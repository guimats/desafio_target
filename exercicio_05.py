def reverse_string(sentence: str) -> str:
    return sentence[::-1]


input_str = str(input('Escreva a frase que deseja inverter: '))
print(f'A string invertida fica:\n{reverse_string(input_str)}')
