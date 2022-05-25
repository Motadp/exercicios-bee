# Leia 4 volores inteiros A, B ,C e D
valores_lidos  = input()

valores_int = [int(x) for x in valores_lidos.split(" ")] # Já deixa todos valores inputados covertido em interiro.

a = valores_int[0] #OBS: a primeira posição sempre começa com ZERO(0)
b = valores_int[1]
c = valores_int[2]
d = valores_int[3]

# A seguir, se B for maior do que C
valido = b > c

# e se D for maior do que A
valido = valido and d > a

# e se C e D, ambos, forem positivos
validos = valido and c > 0 and d > 0

# e se a variável A for par
valido = valido and a % 2 == 0

# escrever  a mensagem "Valores aceitos" ,
# senão escrever ' Valores não aceitos".
if(valido):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")



# a primeira opção
"""
if b > c:
    if d > a:
        if (c + d) > (a + b):
            if (c) (d) < 0:
                print("Valores aceitos")
            else:
                print('Valores não aceitos')        
        
"""                    

