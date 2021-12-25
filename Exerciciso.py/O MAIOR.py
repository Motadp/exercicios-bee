a,b,c = input().split(" ")

a = int(a)
b = int(b)
c = int(c)

num_maior = (a+b+abs(a-b))/2

num_maior = int((num_maior + c + abs(num_maior - c))/2)


print(f"{num_maior} eh o maior")
