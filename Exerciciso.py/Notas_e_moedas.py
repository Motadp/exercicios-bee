m = float(input())

lista_de_notas = [100, 50, 20, 10, 5, 2]

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in lista_de_notas:
    cem = int(m / nota)
    if cem > 0:
        m = m - (nota * cem)
    print(f"{cem} nota(s) de R$ {nota}.00")
print("MOEDAS:")
for moeda in moedas:
   quantidade_moeda = int(round(m,2) / moeda)
   print("{} moeda(s) de R$ {:.2f}".format(quantidade_moeda, moeda))
   m -= quantidade_moeda * moeda