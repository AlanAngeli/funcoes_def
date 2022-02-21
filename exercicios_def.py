"""

Crie uma função1 que receba uma função2 como parâmetro e retorne o valor da função2 executada

"""

def funcao1():
    return "Olá, mundo!"

def funcao2(arg):
    return arg()

executar = funcao2(funcao1)

print(executar)