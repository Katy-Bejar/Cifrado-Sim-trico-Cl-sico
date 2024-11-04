tabla = {
    "A": "11", "B": "12", "C": "13", "D": "14", "E": "15",
    "F": "21", "G": "22", "H": "23", "I": "24", "K": "25",
    "L": "31", "M": "32", "N": "33", "O": "34", "P": "35",
    "Q": "41", "R": "42", "S": "43", "T": "44", "U": "45",
    "V": "51", "W": "52", "X": "53", "Y": "54", "Z": "55"
}

def cifrado_polybios(mensaje):
    return " ".join([tabla.get(letra, "") for letra in mensaje.upper() if letra.isalpha()])

def descifrado_polybios(cifrado):
    tabla_inversa = {v: k for k, v in tabla.items()}
    return "".join([tabla_inversa.get(par, "") for par in cifrado.split()])

# EJERCICIO 4
mensaje = "CRIPTO"
cifrado = cifrado_polybios(mensaje)
print("Cifrado Polybios:", cifrado)
print("Descifrado Polybios:", descifrado_polybios(cifrado))