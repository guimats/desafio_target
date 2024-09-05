'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o
número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua
preferência ou pode ser previamente definido no código;
'''


def is_fibonacci(value: int) -> str:
    s_num1 = 0
    s_num2 = 1

    while True:
        s_num3 = s_num2 + s_num1
        if s_num3 == value:
            return f'Valor {value} pertence a sequência Fibonacci'
        if (value > s_num2 and value < s_num3) or value < 0:
            return f'Valor {value} não pertence a sequência Fibonacci'
        s_num1 = s_num2
        s_num2 = s_num3


input_value = int(input('Informe um valor: '))
print(is_fibonacci(input_value))
