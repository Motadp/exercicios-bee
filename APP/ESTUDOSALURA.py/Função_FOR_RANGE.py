#FOR é um loop, a ideia é definir o valor final e inicial, que o loop aplica automaticamente.
#Para definir o valora incial e final, utilizamos a função RANGE que ira definir a série de valores.

#EX:
for rodada in range(1,10):
    print(rodada)

#Na primeira iteração, o valor da variável rodada será 1, depois 2 e até chegar no valor final,
#obs: Os valores serão contablizados de 1 a 9 no caso ele não leva em consideração o ultimo numero estipulado.

#EX

""""
>>> for rodada in range(1,10):
...     print(rodada)
... 
1
2
3
4
5
6
7
8
9

"""

#Com a função range, podemos definir um step, que é o intervalo entre os elementos, por padrão o step é

#EX

"""
>>> for rodada in range(1,10,2):
...     print(rodada)
... 
1
3
5
7
9

"""

#Mas não necessariamente precisamos usar a função range no for, podemos passar os valor manualmente:

#EX

"""
>>> for rodada in [1,2,3,4,5]:
...     print(rodada)
... 
1
2
3
4
5

"""