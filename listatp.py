'''
Cree una lista con los siguientes elementos: 
conex=[ "127.0.0.1","root","123456","nomina"]
 a) Escriba un programa que imprima todos los elementos de la lista y la longitud total de la lista
conex
 b) Escriba un programa que imprima los elementos ordenados de la lista. (presentación
c) cree otra lista con los elementos en orden inverso (desde el último al 1ero)
d) Encuentre el elemento “root” de la lista y contar cuantos hay?
'''
''''''
# conex=["127.0.0.1" , "root" , "root" ,"123456", "nomina"]
# print(conex)
# print("Cantidad de elementos de la lista: " , len(conex))
# print(sorted(conex))
# listaNueva=[]
# for i in reversed(conex):
#     listaNueva.append(i)
# print(listaNueva)
# cant=0
# for i in conex:
#     if i=="root":
#         cant+=1
# print('''Cantidad de veces que aparece el string "root": ''', cant)

'''
a) cree una lista con los 4 nombres de usuarios del sistema “xxxx”
b) muestre todos los nombres de usuarios. 
c) cree una nueva lista con: la lista ordenada, la lista invertida (del último al primero), los dos 
últimos elementos, los dos primeros elementos
d) agregue un usuario más, y que ese nombre lo ingrese desde el teclado
e) arme una función que le permita agregar usuarios a su lista. 
f) arme una función que le permita buscar un usuario en su lista. 
'''
def agregar(xxxx):
    agregNom=str(input("Ingrese el nombre a agregar: "))
    xxxx.append(agregNom)
    return xxxx

def buscar(xxxx):
    buscarNom=str(input("Ingrese el nombre a buscar: "))
    buscarNom=buscarNom.capitalize()
    if buscarNom in xxxx:
        print("El nombre está en la lista")
    else:
        print("El nombre no se encuentra en la lista")

xxxx=["Flor","Juan","Marce","Noe"]
print("Los nombres de los usuarios son:")
print(xxxx[0],"\n",xxxx[1],"\n",xxxx[2],"\n",xxxx[3])
nuevaLista=[]
for i in (xxxx):
    nuevaLista.append(i)
for i in reversed(xxxx):
    nuevaLista.append(i)
for i in (xxxx[2:4]):
    nuevaLista.append(i)
for i in (xxxx[0:2]):
    nuevaLista.append(i)
print(nuevaLista)
print(nuevaLista.index("Juan"))     #muestra posicion del elemento

exit=0
while exit==0:
    print("Para agregar un nombre ingrese 1, para buscar un nombre ingrese 2, para salir ingrese 3")
    opc=int(input("Ingrese una opcion: "))
    if opc==1:
        agregar(xxxx)
    elif opc==2:
        buscar(xxxx)
    elif opc==3:
        exit+=1
    else:
        print("Opción incorrecta")

