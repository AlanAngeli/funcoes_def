variavel = "valor"

def func():
    print(variavel)

func()

def func2():
    variavel = "outro valor"
    print(variavel)

func2()
print(variavel) #nota-se que a variavel é outra dentro da função def.

def func3():
    global variavel #global faz com que todas essas variáveis sejam uma só, mesmo dentro de um def
    variavel = "mais um valor"
    print(variavel)

func3()
func2()
func()

"""Apesar de tudo, não é uma boa prática"""