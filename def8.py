"""
funções def em  Python

*args,**kwargs


"""

def func(*args):
    for v in args:
        print(v)

lista = [1,2,3,4,5]
func(lista)

###########

def func(*args):
    print(args[0])
    print(args[2])

lista = [1,2,3,4,5]
func(*lista)