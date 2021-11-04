#cadenas

cadena1="cada cosa que leo"
cadena2="cuando estoy al pedo"

print(cadena1+cadena2)
print(cadena1[4:15:2]) #entre corchetes posicion de inicio de conteo, pos final e intervalo
print(len(cadena2)) #cantidad de caracteres
print(cadena2[::-1]) #de atras para delante
print(cadena2[:-3:-1]) #de atras para delante una porcion especifica
print(cadena2[-5:]) #leer derecho contando de atras para delante
print(cadena1.find("cosa")) #cadena.find(subcadena) devuelve posicion
print("cosa" in cadena1) #booleano para saber si una cadena tiene X palabra/caracter. Devuelve ToF
print(cadena1.replace("cosa","palabra")) #reemplazar parte de la cadena. Orden: cadena.replace(subcadena.vieja,subcadena.nueva)
print(cadena1.strip()) #saca los espacios en blanco de adelante y atras
print(cadena1.count("a")) #cuenta la cantidad de veces que aparece la subcadena mencionada en los (). Orden: cadena.count("subcadena")




'''Desarrolle una herramienta que reconozca si un texto es una URL básica bien formada. Entendemos 
por URL un texto que empieza con www. y termina con .com o  .com.ar. En caso de ser una URL no 
formada indique si el error está al principio o al final de la url.'''

url=str(input("Ingrese una URL: "))
url=url.lower()
pcom=(".com")
pcompar=(".com.ar")
doblev=("www.")
final=url[-7:]
finalcorto=url[-4:]
arranque=url[:4]
if arranque==doblev and (final==pcompar or finalcorto==pcom):
    print("la url es correcta")
elif arranque==doblev:
       print("el error esta al final de la url")
else:
    print("el arranque esta mal")

