""" Melhor maneira de substituir a variavel, não usando a função global."""

var = "valor"

def func():
    print(var)

def func2(arg=None):
    arg = arg.replace("v","c")
    return arg

func()
outra_var = func2(arg=var)

print(outra_var)
