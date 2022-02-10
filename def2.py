def divisao (n1,n2):
    return n1 / n2

divide = divisao(8,2)
print(divide)

def soma (n1,n2,n3):
    return n1 + n2 + n3

adicao = soma (10,5,17)
print(adicao)


###################################

def divisao2 (num1,num2): #evitar erro caso o número a dividir seja zero
    if num2 > 0:
        return num1 / num2

divide2 = divisao2(8,0)

if divide2:
    print(divide2)
else:
    print("Conta inválida")