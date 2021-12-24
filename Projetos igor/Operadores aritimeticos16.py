"""
+ : Adição
- : Subitração
* : Multiplicação
/ :Divisão, com ponto Flutuante (float)
//:Divisão, Inteira (Int)
**:Exponenciação/ pentenciação
% :Ele retoma o modululo, o resto da divisão entre um número e outro.
():Alteração de presedencia nas contas
"""
#Exemplos

print ('Multplicação10', 10 * 10)
print('Adição', 10 + 10)
print('Subtração',10 - 10 )
print('Divisão', 10 / 10)
print('Divisão float', 10 / 3)
print('Divisão inteira', 10 // 3)
print('Exponenciação', 2 ** 10 )
print('Retomada do moludo', 10 % 3)

#OBSs

print(20*'A')
print(20*2)
print('20'+'A')
print(20+2)

#OBS, Ordem de precedencia
"""
( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

** - Depois vem a exponenciação

* / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

+  - - Por fim, soma e subtração

 """

 #Exemplo
 
print('ordem de precedencia', 2 + 5 * 3 ** 2 - (23.5 + 23.5))
 
