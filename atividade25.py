import math
a = float(input("Digite um valor para a letra A: " ))
b = float(input("Digite um valor para a letra B: " ))
c = float(input("Digite um valor para a letra C: " ))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print("Não possui raizes.")
elif delta == 0:
    var1 =  -b / (2*a)
    print("A raiz é: ",var1)
else:
    varPosi = (-b + math.sqrt(delta)) / (2* a)
    varNega = (-b + math.sqrt(delta)) / (2* a)
    print("A equação tem duas raizes",varPosi,"e ",varNega)