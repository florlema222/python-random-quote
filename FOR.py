#ESTRUCTURA DE REPETICION FIJA   FOR
'''
for variable in secuencia:   #secuencia indica la cantidad de veces que se va a repetir el código
    repetir algo
se dice que es FIJA porque el for siempre tiene un valor fijo que indica la cant de veces que se va a repetir el codigo
'''
for i in "aeiou":
    print(i)
for i in range(10): #range indica el rango desde donde hasta donde imprimir (solo para numeros (checkear))
    print(i)
for i in range(3,12): #imprime del 3 al 11
    print(i)
num=2
for i in range(num,num*3): #el rango puede ser armado con operaciones matematicas tmb
    print(i)


#sumar una cantidad de numeros especifica con for
cant=int(input("Ingrese la cantidad de numeros a sumar; ")) 
suma=0 #determino la variable suma y la arranco en 0
for i in range(cant):
    num=int(input("Ingrese el numero:"))
    suma=num+suma #el loop va modificando el valor de suma agregandole la sumatoria de cada valor ingresado como num
print("La sumatoria de los ", cant, " números es: ", suma)

