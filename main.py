
def contar_caracteres(frase):
    """Devuelve el número total de caracteres de la frase."""
    return len(frase)


def contar_vocales(frase):
    """Cuenta las vocales de la frase."""
    vocales = "aeiouáéíóúü"
    contador = 0

    for letra in frase.lower():
        if letra in vocales:
            contador += 1

    return contador


def contar_consonantes(frase):
    """Cuenta las consonantes de la frase."""
    vocales = "aeiouáéíóúü"
    contador = 0

    for letra in frase.lower():
        if letra.isalpha() and letra not in vocales:
            contador += 1

    return contador


def contar_digitos(frase):
    """Cuenta los dígitos de la frase."""
    contador = 0

    for caracter in frase:
        if caracter.isdigit():
            contador += 1

    return contador


def contar_espacios(frase):
    """Cuenta los espacios de la frase."""
    contador = 0

    for caracter in frase:
        if caracter == " ":
            contador += 1

    return contador


def letra_mas_repetida(frase):
    """Devuelve la letra que más se repite."""
    frecuencias = {}

    for letra in frase.lower():
        if letra.isalpha():
            frecuencias[letra] = frecuencias.get(letra, 0) + 1

    if not frecuencias:
        return "No hay letras"

    mayor = max(frecuencias.values())

    for letra, cantidad in frecuencias.items():
        if cantidad == mayor:
            return letra


def es_palindromo(frase):
    """Comprueba si la frase es un palíndromo ignorando espacios y mayúsculas."""
    texto = frase.replace(" ", "").lower()
    return texto == texto[::-1]


def invertir_frase(frase):
    """Devuelve la frase al revés utilizando un bucle."""
    invertida = ""

    for caracter in frase:
        invertida = caracter + invertida

    return invertida


def main():
    """Solicita una frase y muestra su informe completo."""
    frase = input("Introduce una frase: ")

    print("\n===== INFORME DE LA FRASE =====")
    print("Caracteres:", contar_caracteres(frase))
    print("Vocales:", contar_vocales(frase))
    print("Consonantes:", contar_consonantes(frase))
    print("Dígitos:", contar_digitos(frase))
    print("Espacios:", contar_espacios(frase))
    print("Letra más repetida:", letra_mas_repetida(frase))

    if es_palindromo(frase):
        print("¿Es palíndromo?: Sí")
    else:
        print("¿Es palíndromo?: No")

    print("Frase al revés:", invertir_frase(frase))


main()
