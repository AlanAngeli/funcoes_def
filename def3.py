def divisao (n1, n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao (8,4)
if divide:
    print(divide)
else:
    print("Inválido")

##############

#def f(var):
#    print(var)

#def db():
#   return f

#var = db()("Função aqui")

#######################

def dumb():
    return [1,2,3,4,5]

var = dumb()
print(dumb(), type(dumb()))