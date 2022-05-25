""""
numero = int(input())

a = numero

cem = int(a / 100)
if cem > 0:
    a = a - (100 * cem)

cinquenta = int(a / 50)
if cinquenta > 0:
    a = a - (50 * cinquenta)

vinte = int(a / 20)
if vinte > 0:
    a = a - (20 * vinte)

dez = int(a / 10)
if dez > 0:
    a = a - (10 * dez)

cinco = int(a / 5)
if cinco > 0:
    a = a - (5 * cinco)


dois = int(a / 2)
if dois > 0:
    a = a - (2 * dois)

um = int(a / 1)
if um > 0:
    a = a - (1 * um)

print(numero)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{cinquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")

"""

### Primeira opção

numero = int(input())

a = numero

lista_de_notas = [100, 50, 20, 10, 5, 2, 1]

print(numero)
for nota in lista_de_notas:
    cem = int(a / nota)
     - (nota * cem)
    print(f"{cem} nota(s) de R$ {nota},00")
