def cifrado_cesar(mensaje, desplazamiento):
    cifrado = ""
    for letra in mensaje:
        if letra.isalpha(): 
            desplazada = ord(letra) + desplazamiento
            if letra.isupper():
                cifrado += chr((desplazada - 65) % 26 + 65)
            else:
                cifrado += chr((desplazada - 97) % 26 + 97)
        else:
            cifrado += letra
    return cifrado

def descifrado_cesar(mensaje, desplazamiento):
    return cifrado_cesar(mensaje, -desplazamiento)

# EJERCICIO 1
mensaje = "SEGURIDAD"
desplazamiento = 3
cifrado = cifrado_cesar(mensaje, desplazamiento)
print("Cifrado César:", cifrado)
print("Descifrado César:", descifrado_cesar(cifrado, desplazamiento))