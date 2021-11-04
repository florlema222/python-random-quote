#WHILE

#sumar numeros ingresados

num=int(input("Ingrese numeros, ponga 0 para terminar: "))
suma=0
while num!=0:
    suma=num+suma
    num=int(input("Ingrese numeros, ponga 0 para terminar: ")) #tengo que volver a meter la orden de ingreso adentro del loop sino se clava
print("La suma es: ", suma)



