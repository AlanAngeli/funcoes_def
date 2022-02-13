"""

Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função
por divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e 3, retorne FizzBuzz, caso cotrário,
retorne o número enviado.

"""

def fizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz", n, "é divisível por 5 e 3"
    elif n % 5 == 0:
        return "buzz", n, "é divisível por 5"
    elif n % 3 == 0:
        return "fizz", n, "é divisível por 3"
    else:
        return n

from random import randint

for i in range(10):
    aleatorio = randint(0,100) #gerar números aleatórios entre 0 a 100, sendo 10 números gerados
    print(fizzBuzz(aleatorio))



#modo mais limpo de escrever o mesmo código
#    if n % 3 == 0 and n % 5 == 0:
#        return "fizzbuzz", n, "é divisível por 5 e 3"
#    if n % 5 == 0:
#        return "buzz", n, "é divisível por 5"
#    if n % 3 == 0:
#        return "fizz", n, "é divisível por 3"
#    return n


