#OBS len NÃO funciona com tipos numericos.
#len é utilizado para contar caracteres.
""""
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))
"""
#Limite de caracteres.
"""
usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 cartacteres')
else:
    print('você foi cadastrado no sistema. ')    

"""


string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')







