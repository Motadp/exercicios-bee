# 1019 Conversão de Tempo

"""
numero = int(input())

a = numero

lista_de_horas = [3600, 60, 1]

for horas in lista_de_horas:
    temp = int(a / horas)
    if temp < a:
        a = (a - (60 * m))
        
        
        print(f' {temp}')

""" 
# 1019 Conversão de Tempo

"""

temp = int(input())

a = temp

h = int(a / 3600)

m = int(a / 60)
if m < 60:
    a = int(a - (100 * m))


s = int(a - (60 / m))

print(f'{h}:{m}:{s}')

"""
# 1019 Conversão de Tempo


n = int(input())
h = n // 60**2
n = n - h * 60**2

m = n // 60
n = n - m*60

s = n

print('{}:{}:{}'.format(h, m, s))




# 1019 Conversão de Tempo
segundos = int(input())

horas = segundos//(60*60)
segundos = segundos%(60*60)

minutos = segundos//60
segundos = segundos%60

print(f"{horas}:{minutos}:{segundos}")