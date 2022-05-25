"""
Condições IF, ELIF e ELSE
"""

""""
if False:
    print('Verdadeiro.') #Atravez do if Flase essa linha não seria excutada, por ser falso.
print ('A minha espressão não é verdadeira.')
"""

""""
if False:
    print('Verdadeiro.')
else:
    print("não é verdadeiro.")
"""


if False:
    print('Verdadeiro.')
    print('teste teste2')
elif True:
    print("Agora é verdadeiro.")
    nome = input("Qual o seu nome")

    print(f'Seu nome é {nome}.')
elif True:
    print('Mais uma verdade')
    print(22+22)    
else: # O else será aplicado caso todas as informações anteriores sejam falsas.
    print("Não é verdadeiro.")

      
