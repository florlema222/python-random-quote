# #listas
# letras=list("ABC")
# print(letras)

enteros=[1,2,3,4,5] #lista que se va a ir armando segun lo que se ingrese

def mostrarLista(lista): #modulo para mostrar lo que compone la lista
    print(lista)

def cargarElementos(lista): #modulo para rellenar lista, tiene dos posibles parametros: lista y elementos, puedo usar ambos o uno
    elemento=int(input("Ingrese un elemento: "))
    lista.append(elemento)                      #append es para agregar un elemento a la lista
    return lista                        #devuelve la lista

def cargarVarios(lista):
    aux=input("cargar varios elementos separados por , : ")
    elemento=list(aux) #me arma lista pero considera las comas (,) como elementos de la lista
    elemento=aux.split(",") #uso el split para separar los elementos cortando cada vez que haya coma, salen como str
    for x in elemento:          #para transformar cada elemento en int si o si tengo que hacer pasar la lista uno por uno con for
        lista.append(int(x))    #le digo que vaya agregando a la variable lista cada elemento pasado a int
    return lista

def borrarElemento(lista):
    aux=int(input("Ingrese el elemento a borrar: "))
    lista.remove(aux)
    return lista

def sumarElementos(lista):
    suma=0                      #en los def la variable suma va adentro
    for i in lista:             #para que sume los comp de la lista, el for lo recorro por la lista
        suma=i+suma
    return suma

def multiploElemento(lista):
    num=input("Ingrese un numero")
    elemento=list(num)
    for i in elemento:
        lista.append(int(i))
    return lista

def multiploSI(lista):
    nuevo=multiploElemento
    for i in nuevo:
        lista.append()

print("elija una opcion: ")
print("1. Mostrar lista")
print("2.Cargar elemento")
print("3.Cargar varios elementos al final")
print("4.Eliminar algun elemento de la lista")
print("5.Sumar elementos")
print("9. Salir")
exit=0

while(exit==0):         #determino el valor en 0 de exit para poder salir del while con la opcion 9 (linea37/38)
    opcion=int(input("Ingrese una opcion: "))   #esto va dentro de la condicion sino se loopea la opcion ingresada y no corta
    if opcion==1:
        mostrarLista(enteros)
    elif opcion==2:
        cargarElementos(enteros)
    elif opcion==3:
        entreros=cargarVarios(enteros)
    elif opcion==4:
        borrarElemento(entreros)
    elif opcion==5:
        sumarElementos(entreros)
        print("La suma es ", sumarElementos)
    elif opcion==6:
        multiploElemento(enteros)
        

    elif opcion==9:
        exit=1
    else:
        print("Opcion incorrecta")         #como exit sigue valiendo 0, renueva ciclo, a paso seguido vuelve a solicitar ingresar opcion
print("fin")




