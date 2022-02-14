def func(*args,**kwargs):
    print(args)

    idade = kwargs.get("idade")
    nome = kwargs.get("nome")

    print(nome)
    if idade is not None:
        print(idade)
    else:
        print("Idade não exste")

lista = [1,2,3]
func(*lista, nome = "Alan", idade = 31)

#func(*lista, nome = "Alan", idade = None)



