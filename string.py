'''
a="cadena"
longitudTotal=len(a)
print(longitudTotal)
print(a[::-1])
print(a.replace ("de" , "ca"))
print(a.upper())
print(a.lower())
print(a.count("a"))
'''
'''
cadena=str(input("Ingrese una frase: "))
cant=0
for x in cadena.lower():
    if x in "a":
        cant+=1
print("cantidad de as: ", cant)

jercicio 1
a) Construya un programa que lea los 10 primeros números naturales y determinar su suma.
b) Modifique el programa anterior para que muestre el promedio de los pares y el promedio de los
impares


suma=0
for x in range(1,11):
    print (x)
    suma=suma+x
print(suma)

'''

'''sumar los multiplos de 3 hasta el 30 inclusive'''
'''
for x in range(0,31,3):
    print(x)
'''
'''
for x in range(1,11):
    print(x)

print("Ahora los impares")
suma=0
cant=0
for x in range(1,11,2):
    print(x)
    suma=suma+x
    cant+=1
print(suma/cant)

print("Ahora los pares")
suma=0
cant=0
for x in range(0,11,2):
    print(x)
    suma=suma+x
    cant+=1
print(suma/cant)
'''
'''
Dado un número N calcular su factorial. Utilizar ciclo definido, estructura For y variable acumuladora del 
producto.
Ejemplo: 4! =4*3*2*1 = 24

'''
'''
num=int(input("Ingrese un numero: "))
factorial=1
for x in range(1,num+1):
    print(x)
    factorial*=x
print(factorial)

'''
import random
for i in range(10):
    print(random.randrange(0,50))


