
"""

Criar uma função que exiba saudação  com os parâmetros saudacao e nome

"""

def saudacao (saudacao, nome):
    print(saudacao, nome)

saudacao("Olá,", "Alan!")
saudacao("Olá,", "Eloisa!")

"""

Criar uma função  que receba 3 números como parâmetros  e exiba a soma entre eles

"""

def soma(n1, n2, n3):
    print (n1+ n2 + n3)

soma(1,2,3)
soma(4,1,3)
soma(3,7,2)

"""

Crie uma função que receba 2 números, sendo o primeiro  um valor e o segundo percentual. Retorne (return)
o valor do primeiro número somado do aumento do percentual do mesmo

"""

def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))

aumento_percentual(50, 100)
aumento_percentual(100, 10)
aumento_percentual(50, 10)
aumento_percentual(15, 100)
