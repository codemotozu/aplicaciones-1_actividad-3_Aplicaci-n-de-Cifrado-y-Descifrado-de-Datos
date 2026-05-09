"""
logica.py
Módulo de lógica para el cifrado y descifrado de números de 6 dígitos.
Maestría en Inteligencia Artificial - Aplicaciones I
"""


def cifrar_numero(numero_str: str) -> str:
    """
    Cifra un número entero de 6 dígitos.

    Proceso:
      1. A cada dígito se le suma 7 y se obtiene el residuo mod 10.
      2. Se intercambian posiciones: 1°↔3°, 2°↔4°, 5°↔6°.

    Parámetros:
        numero_str (str): Cadena de 6 dígitos.

    Retorna:
        str: Número cifrado como cadena de 6 caracteres.
    """
    # Paso 1: sumar 7 y aplicar módulo 10 a cada dígito
    digitos = [(int(d) + 7) % 10 for d in numero_str]

    # Paso 2: intercambiar posiciones
    # Posición 0 ↔ Posición 2
    digitos[0], digitos[2] = digitos[2], digitos[0]
    # Posición 1 ↔ Posición 3
    digitos[1], digitos[3] = digitos[3], digitos[1]
    # Posición 4 ↔ Posición 5
    digitos[4], digitos[5] = digitos[5], digitos[4]

    return "".join(str(d) for d in digitos)


def descifrar_numero(numero_cifrado_str: str) -> str:
    """
    Descifra un número previamente cifrado con cifrar_numero().

    Proceso inverso:
      1. Se revierten los intercambios de posición: 1°↔3°, 2°↔4°, 5°↔6°.
      2. A cada dígito se le resta 7 (equivalente a sumar 3) mod 10.

    Parámetros:
        numero_cifrado_str (str): Cadena cifrada de 6 dígitos.

    Retorna:
        str: Número original como cadena de 6 caracteres.
    """
    digitos = [int(d) for d in numero_cifrado_str]

    # Invertir intercambios (mismas posiciones, orden no importa aquí)
    digitos[4], digitos[5] = digitos[5], digitos[4]
    digitos[1], digitos[3] = digitos[3], digitos[1]
    digitos[0], digitos[2] = digitos[2], digitos[0]

    # Restar 7 mod 10 (equivale a sumar 3 mod 10)
    digitos = [(d - 7) % 10 for d in digitos]

    return "".join(str(d) for d in digitos)


def validar_entrada(texto: str) -> bool:
    """
    Valida que la entrada sea exactamente 6 dígitos numéricos.

    Parámetros:
        texto (str): Cadena a validar.

    Retorna:
        bool: True si es válida, False en caso contrario.
    """
    return texto.isdigit() and len(texto) == 6
