n = (input())
s = int(input())
v = float(input())
bv = (((v * 1.15) - v) + s) 

print(f'NOME = {n}')
print("TOTAL = R$ %0.2f" %bv)