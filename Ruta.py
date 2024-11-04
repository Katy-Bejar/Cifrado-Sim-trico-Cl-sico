def cifrar_por_ruta(mensaje, filas, columnas):
    matriz = [['' for _ in range(columnas)] for _ in range(filas)]
    idx = 0

    # Llena la matriz con los caracteres del mensaje
    for i in range(filas):
        for j in range(columnas):
            if idx < len(mensaje):
                matriz[i][j] = mensaje[idx]
                idx += 1
    return ''.join(''.join(fila) for fila in matriz)

# EJERCICIO 6
mensaje = "ATAQUETEMPRANO"
filas = 3
columnas = 4
cifrado = cifrar_por_ruta(mensaje, filas, columnas)
print("Salida cifrada:", cifrado)