""""
Funções de formatação de strings
"""""
nome = 'Igor Mota'
idade = 25 # int
altura = 1.80 #float
e_maior = idade >18 #bool
peso = 85
imc = peso / (altura ** 2)

print(nome, 'tem', idade,'idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {}'. format(nome, idade, imc)) # O python já compreende que a ordem em que as variveis econtra-se será a mesm utilizada na chaves.
# Ex Na primeira chave {nome}, na segunda chave {idade}, na terceira chave {imc}. 
print('{0} tem {1} anos de idade e seu imc é {2}'. format(nome, idade, imc)) # Cada variavel representa um numero nesse caso, 0 = nome, 1 = idade, 2 = imc.
print('{n} tem {i} anos de idade e seu imc é {imc}'. format(n=nome, i=idade, im=imc)) # Cada variavel será expecificada como uma letra.
