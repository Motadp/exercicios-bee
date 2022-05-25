numero = int(input())
print(int(numero/365))
print(int((numero%365)/30))
print(int((numero%365)%30))

# Dias em anos

"""
n = int(input())

a = n // 365
n = n - a*365

m = n // 30
n = n - m*30

d = n

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))

"""