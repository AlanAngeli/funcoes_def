"""
funções def em  Python

*args,**kwargs


"""

def funcao (a1, a2, a3, a4, a5, a6, nome = None, idade = None):
    return  a1, nome, idade,

variavel_da_funcao =  funcao(1,2,3,4,5,6, nome = "Alan", idade = "31")
print(variavel_da_funcao[1], variavel_da_funcao[2])
print(variavel_da_funcao)

############################
"""     args            """

def func(*args):
    print(args)

lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1, n2, n) #o restante da lista está em n

print(*lista, sep="-") #sep é o separador
print(*lista, sep="*")
print(*lista, sep="$$$")






