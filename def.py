def funcao_teste():
    print("Pugs são fofos")

funcao_teste() #chamando a função def criada
funcao_teste()
funcao_teste()

def dados(nome, idade, sexo):
    print(nome, idade, sexo)

dados("Alan", "31", "Masculino")
dados("Eloisa", "30", "Feminino")

def dados2(nome = "Klelson", idade = "33", sexo = "Masculino"):
    print(nome, idade, sexo)

dados2()

def dados3(nome = "Klelson", idade = "33", sexo = "Masculino"):
    nome = nome.replace("e","30")
    idade = idade.replace("3","E")
    sexo = sexo.replace("Masculino", "Feminino")
    print(nome, idade, sexo)

dados3()


