'''Ejercicio a)


lista = 0                                       #las listas vacias van con [], sino diria que la variable lista=0
for i in range[4]                               #faltan los dos puntos y el range se usa con parentesis
print (Dime una palabra)                        #identar - no print sino input de un string entre ""
lista = lista + palabra                         #identar - para agregar cosas a la lista solo se agrega .append(lo que agrego)
print (Las palabras escritas son lista)         #faltan comillas del string y llamar a la variable lista
'''


lista=[]
for i in range(4):
    palabra=str(input("Dime una palabra: "))
    lista.append(palabra)
print ("las palabras escritas son: ", lista)

'''Ejercicio b)
                                                                        #Declarar el valor de contador en 0
for i in range[3,10]                                                    #identar - parametros de range entre parentesis y :
contador = 1 + contador                                                 #identar - para sumar se coloca variable+=numero a sumar en cada pasada
print (Por ahora contador vale contador pero todavía no he terminado)   #COmillas, citar variable con comas
print (En total, contador vale contador)'''
    
contador=0
for i in range(3,10):
    contador+=1
    print("Por ahora el contador vale ", contador, " pero todavia no he terminado")
print("En total , contador vale ", contador)