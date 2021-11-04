#Libreria OS
import os

a=os.getcwd() # devuelve el directorio de trabajo actual
print(a)
os.listdir() # devuelve la lista de archivos y carpetas del directorio
path = "/home/florencia/Documentos"
os.chdir(path)   # cambia el directorio de trabajo
os.getcwd()  # imprime el directorio de actual
os.chdir(a) # cambia el directorio de trabajo guardado en a
os.getcwd
ruta = os.getcwd()  # obtiene ruta del script
contenido = os.listdir(ruta) # guardo en una lista los archivos de directorio:ruta
print(ruta) # imprimo posición del script
print(contenido) # imprimo la lista

'''
Ejercicio 2:
Utilice las librería que crea necesario para:
a) posicionarse en el directorio Documentos, pero guarde el actual
b) ejecute el comando ls y colóquelo en una lista
c) cuente los archivos con nombre mayor a 6 caracteres
d) luego vuelva a directorio inicial
'''
contador=0
listadegrandes=[]
for i in contenido:
    if len(i)>6:
        listadegrandes.append(i)
        contador+=1
print(contador)
print(listadegrandes)

