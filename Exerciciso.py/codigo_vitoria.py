numero = int(input())

a = numero

lista_de_notas = [100, 50, 20, 10, 5, 2, 1]

print(numero)
for nota in lista_de_notas:
    cem = int(a / nota)
    if cem > 0:
        a = a - (nota * cem)
    print(f"{cem} nota(s) de R$ {nota},00")
