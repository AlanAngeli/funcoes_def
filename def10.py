def func(*args,**kwargs):
    print(args)

    idade = kwargs.get("idade")


    if idade is not None:
        print(idade)
    else:
        print("Idade não exste")

lista = [1,2,3]
func(*lista, idade = None)

