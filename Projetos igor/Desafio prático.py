nome = 'Igor'
idade = 25
peso = 84
altura = 1.79 
ano = 2021
nascimento = ano - idade
imc = peso / (altura ** 2)

print('Aluno {}, ano de entrada {}, tem como objetivo a perda de peso e hipertrofia.'. format(nome, ano)) 
print(f'Peso atual: {peso}kg, baixar para 75kg.')
print('Altura {}.'. format(altura))
print(f'Ano de nascimento: {nascimento}.')
print(f'Percentual de IMC: {imc:.2f}.')