
a,b,c = input().split(" ")

num_maior = (a+b+abs(a-b))/2

num_maior = (num_maior + c + abs(num_maior - c))/2

print(f"{num_maior} eh o maior")


