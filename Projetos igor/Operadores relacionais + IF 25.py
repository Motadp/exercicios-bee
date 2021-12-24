""""
Operadores relacionais - Aula 4
 == igualdade > maior que 
 >= maior que ou igual a 
 < menor que 
 <= menor que igual a 
 != difente
 """
"""""
print ( 2 == 2 ) # OBS: Sinal de = repsente que uma cois é igual a outra.
  # OBS: Quando o sinal de = for utilizado dessa maneira == sinificara um questionamento. Ex: Dois é igual a dois?  2 == 2 ? 
"""
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade?' )

idade = int (idade)

# Limite para pegar emprestimo
idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} Não pode pegar emprestimo.')
