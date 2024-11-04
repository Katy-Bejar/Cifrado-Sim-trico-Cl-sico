def crear_matriz_clave(clave):
    clave = ''.join(sorted(set(clave.upper()), key=clave.index)).replace('J', 'I')
    alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Alfabeto sin 'J'
    matriz = []

    for letra in clave + alfabeto:
        if letra not in matriz:
            matriz.append(letra)

    # Convertir a una matriz 5x5
    return [matriz[i:i+5] for i in range(0, 25, 5)]

def obtener_posicion(matriz, letra):
    for fila in range(5):
        for columna in range(5):
            if matriz[fila][columna] == letra:
                return fila, columna
    return None, None

def cifrar_par_playfair(matriz, par):
    f1, c1 = obtener_posicion(matriz, par[0])
    f2, c2 = obtener_posicion(matriz, par[1])

    if f1 == f2:
        return matriz[f1][(c1 + 1) % 5] + matriz[f2][(c2 + 1) % 5]
    elif c1 == c2:
        return matriz[(f1 + 1) % 5][c1] + matriz[(f2 + 1) % 5][c2]
    else:
        return matriz[f1][c2] + matriz[f2][c1]

def preparar_mensaje_playfair(mensaje):
    mensaje = mensaje.replace("J", "I").upper()
    preparado = ""
    i = 0
    while i < len(mensaje):
        preparado += mensaje[i]
        # Agregar 'X' si hay letras duplicadas o al final si es impar
        if i + 1 < len(mensaje) and mensaje[i] == mensaje[i + 1]:
            preparado += "X"
        elif i + 1 < len(mensaje):
            preparado += mensaje[i + 1]
            i += 1
        i += 1
    if len(preparado) % 2 != 0:
        preparado += "X"
    return preparado

def cifrar_playfair(mensaje, clave):
    matriz = crear_matriz_clave(clave)
    mensaje_preparado = preparar_mensaje_playfair(mensaje)
    cifrado = ""
    for i in range(0, len(mensaje_preparado), 2):
        cifrado += cifrar_par_playfair(matriz, mensaje_preparado[i:i + 2])
    return cifrado

# EJERCICIO 3
mensaje = "ATAQUEINMINENTE"
clave = "SEGURIDAD"
cifrado = cifrar_playfair(mensaje, clave)
print("Cifrado Playfair:", cifrado) 