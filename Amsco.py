def dividir_bloques_amsco(mensaje):
    """Divide el mensaje en bloques de 1 o 2 caracteres de forma alternada."""
    bloques = []
    alterna = True
    i = 0
    while i < len(mensaje):
        tamaño = 1 if alterna else 2
        bloques.append(mensaje[i:i+tamaño])
        i += tamaño
        alterna = not alterna
    return bloques

def ordenar_bloques(bloques, clave):
    """Reordena los bloques segun la clave numerica."""
    columnas = [[] for _ in range(len(clave))]
    for i, bloque in enumerate(bloques):
        columnas[i % len(clave)].append(bloque)
    
    columnas_ordenadas = [col for _, col in sorted(zip(clave, columnas))]
    return ''.join([''.join(col) for col in columnas_ordenadas])

def imprimir_formato(mensaje, clave, cifrado):
    bloques = dividir_bloques_amsco(mensaje)
    clave_numerica = [int(d) for d in str(clave)]
    
    columnas = [[] for _ in clave_numerica]
    for i, bloque in enumerate(bloques):
        columnas[i % len(clave_numerica)].append(bloque)
    
    print(f"MENSAJE ENTRADA: \"{mensaje}\"")
    print(f"CLAVE NUMÉRICA: {clave}")
    print(f"MENSAJE SALIDA -> \"{cifrado}\"")
    print("\n", " ".join(str(d) for d in clave_numerica))
    
    max_filas = max(len(col) for col in columnas)
    for fila in range(max_filas):
        fila_texto = []
        for col in columnas:
            fila_texto.append(col[fila] if fila < len(col) else " ")
        print(" ".join(fila_texto))

def cifrar_amsco(mensaje, clave):
    clave_numerica = [int(d) for d in str(clave)]
    bloques = dividir_bloques_amsco(mensaje)
    cifrado = ordenar_bloques(bloques, clave_numerica)
    imprimir_formato(mensaje, clave, cifrado)

# EJERCICIO 5
mensaje = "ESTOYSEGURO"
clave = 321
cifrar_amsco(mensaje, clave)