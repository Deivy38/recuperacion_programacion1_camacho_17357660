def ordenar_insercion(arreglo):
    for indice in range(1, len(arreglo)):
        valor_actual = arreglo[indice]
        posicion = indice - 1
        while posicion >= 0 and arreglo[posicion] > valor_actual:
            arreglo[posicion + 1] = arreglo[posicion]
            posicion -= 1
        arreglo[posicion + 1] = valor_actual

digitos_cedula = "17357660"

calificaciones = []
for i in range(len(digitos_cedula)):
    digito = int(digitos_cedula[i])
    posicion = i + 1
    calificaciones.append(digito * posicion)

print("Lista original de calificaciones:", calificaciones)

ordenar_insercion(calificaciones)

print("Lista ordenada con insercion:", calificaciones)