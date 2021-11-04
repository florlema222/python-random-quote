"""
Ejercicio 1:
Utilizando estructura de repetición con ciclo indefinido, genere un menú que ofrezca la selección de las 
siguientes opciones
a) armar una lista con 10 elementos generados al azar con la función random, elementos entre 0 y 100
b) imprimir la lista ordenada 
c) hallar el porcentaje de los impares
d) hallar la cantidad de números primos
"""
import random
lista=[]            #corchetes para listas si o si
for elementos in range(10):                #entre parentesis la cantidad de pasadas que hace, o sea la cant de valores que quiero guardar en la lista luego
    lista.append(random.randrange(100))
print(lista)

def mostrar(lista):
    print(lista)
    return lista

def orden(lista):
    print(sorted(lista))
    return sorted(lista)

def impares(lista):
    divisor=0
    for i in (lista):
        if i%2==1:
            divisor+=1
    print("hay" , divisor, "numeros inpares en la lista")
    porcen=divisor*10
    return porcen

def primos(num):
    cant=0
    for i in range(1,num):
        if num%i==0:
            cant+=1
            if cant>1:
                return False
    return True
            
exit=0
print('''Ingrese una opción:
1) armar una lista con 10 elementos generados al azar con la función random, elementos entre 0 y 100
2) imprimir la lista ordenada 
3) hallar el porcentaje de los impares
4) hallar la cantidad de números primos
5) Salir''')

while(exit==0):         #determino el valor en 0 de exit para poder salir del while con la opcion 9 (linea37/38)
    opcion=int(input("Ingrese una opcion (5 para salir): "))
    if opcion==1:
        mostrar(lista)
    elif opcion==2:
        orden(lista)                      
    elif opcion==3:
        print("El porcentaje de num impares es: " , impares(lista), "%")
    elif opcion==4:
        cant=0
        listaPrimos=[]
        for i in lista:
            if primos(i)==True:
                cant+=1
                listaPrimos.append(i)
        print("Los números primos de la lista son: " ,listaPrimos)        
        print("Un total de " ,cant, "numeros primos")
    elif opcion==5:
        exit+=1
    else:
        print("Opcion incorrecta")         #como exit sigue valiendo 0, renueva ciclo, a paso seguido vuelve a solicitar ingresar opcion

print("Fin")
