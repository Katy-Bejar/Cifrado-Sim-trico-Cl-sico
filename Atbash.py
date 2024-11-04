def cifrado_atbash(mensaje):
    cifrado = ""
    for letra in mensaje:
        if letra.isalpha():
            if letra.isupper():
                cifrado += chr(90 - (ord(letra) - 65))
            else:
                cifrado += chr(122 - (ord(letra) - 97))
        else:
            cifrado += letra
    return cifrado

def descifrado_atbash(mensaje):
    return cifrado_atbash(mensaje)

# EJERCICIO 2
mensaje = "CRIPTOSISTEMA"
cifrado = cifrado_atbash(mensaje)
print("Cifrado Atbash:", cifrado)
print("Descifrado Atbash:", descifrado_atbash(cifrado))
