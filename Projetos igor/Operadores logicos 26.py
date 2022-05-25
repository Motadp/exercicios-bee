""""
Operadores Lógicos - Aula 4
and, or, not
in e not in

"""
# and = Comparação
# ex: (Verdadeiro e False) = Falso
# ex: (Verdadeiro e Verdadeiro) = Verdadeiro
# comparação and comparação2

"""
In[2]: a = 2
In[3]: b = 2
In[4]: c = 3

In[5]:a == b and b < c
Out[5]: True

In[6]:a == b or b < c
Out[6]: True

In[7]: not a == b and not b < c
Out[7] False
"""


"""
# Verdadeiro ou Falso
Comp1 OR Comp2


# Operador NOT

a = 2
b = 3

if b > a:
    print('B é mairo do que A.')
    else:
        print('A é maior do que B.')


"""
"""
# NOT IN
nome = 'Luiz Otávio.' 

if 'Otá' not in nome:
    print("Existe")
else:
    print("Não existe.")    
"""

usuario =   input('Nome de usuário ')
senha =   input('Senha de usuário ')

usuario_bd = 'Luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce está logando no sistema')
else:
    print('Usuário ou senha inválidos.')

