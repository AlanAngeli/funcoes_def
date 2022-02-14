"""
funções def em  Python

*args,**kwargs


"""

def func(*args, **kwargs):
     print(args)
     #print(kwargs["nome"], kwargs["idade"])
     #ou:
     nome = kwargs.get("nome")
     idade = kwargs.get("idade")
     print(nome, idade)


lista = [1,2,3,4,5]
lista2 = [250,500,750,1000]
func(*lista, *lista2, nome = "Alan", idade = 31)
