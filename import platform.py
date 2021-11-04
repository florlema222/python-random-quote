'''

for i in range(10):
    print(random.randint(1,7))
    
aleatorio=random.randint(1,10)
entrada=0

while entrada != aleatorio:
    entrada=int(input("Adivine el número del 1 al 10: "))
    if aleatorio == entrada:
        print("Adivinaste")
    else:
        print("Sigue intentando")
'''
#otra forma mas corta
import random
aleatorio=random.randint(1,10)          #arranca igual
entrada=0

while entrada != aleatorio:             #poner asi significa que mientras que no adivinas pasa esto...
    entrada=int(input("Ingrese un número: "))

print("Adivinaste")
