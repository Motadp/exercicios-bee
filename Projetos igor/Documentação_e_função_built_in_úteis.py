
# isnumeric isdigit isdecimal.
# OBS: Somente serão checados numero e positivos (1234567)

"""
num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

print(num1.isnumeric())
print(num2.isnumeric())
"""
"""
if num1.isdigit() and num2.isdigit():
    nume1 = int(num1)
    nume2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter os números para realizar contas') 
"""
num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print("ERROR")    
