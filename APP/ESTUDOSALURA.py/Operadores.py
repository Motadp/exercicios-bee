#Qual é o tipo dessa variável?

acertou = (chute == numero_secreto)

#Uma variável do tipo bool pode ter apenas dois valores, True ou False, que podemos usar diretamente:

passou = True
errou = False

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# O problema é que a instrução else não aceita receber uma condição. Nesse caso, para resolver o problema do código,
#precisamos trocar para a instrução elif:

usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")