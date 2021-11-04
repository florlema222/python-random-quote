#Listas Teoria
una_lista_vacia=[]
otra_lista_vacia=list()
lista_con_elementos=["hola",254,True,8.4]
lista_string=list("palabra")                #genera lista con cada letra de la palabra
lista_rango=list(range(8))                  #genera lista con los numeros del 0 al 7
lista1=["lun","mart", "mier","juev"]

print(una_lista_vacia)
print(lista_con_elementos)
print(otra_lista_vacia)
print(lista_string)
print(lista_rango)


#Dos formas de recorrer la lista
for i in range(len(lista1)):        #el for frena cuando recorre toda la longitud de la lista
    print(lista1[i])

i=0
while i<len(lista1):                #el while tengo que aclarar primero el valor de i e ir sumandole para que se de la condicion de i<len
    print(lista1[i])
    i+=1

