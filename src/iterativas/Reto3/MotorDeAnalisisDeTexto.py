#Reto 3

import string
from collections import Counter


def limpiar_texto(texto: str, signos_a_remover: str = ",.;!") -> str:
    tabla_limpieza = str.maketrans("", "", signos_a_remover)
    return texto.lower().translate(tabla_limpieza)


def obtener_frecuencias(texto: str, signos_a_remover: str = ",.;!") -> dict:
    texto_limpio = limpiar_texto(texto, signos_a_remover)
    palabras = texto_limpio.split()
    return dict(Counter(palabras))


def obtener_palabra_top(frecuencias: dict) -> tuple[str, int] | tuple[None, int]:
    if not frecuencias:
        return None, 0
    palabra = max(frecuencias, key=frecuencias.get)
    return palabra, frecuencias[palabra]


def main():
    texto_usuario = input("Ingrese una frase o párrafo largo: ")
    frecuencias = obtener_frecuencias(texto_usuario)
    palabra_top, conteo_top = obtener_palabra_top(frecuencias)

    if palabra_top:
        print(f"Diccionario de frecuencias: {frecuencias}")
        print(f"Palabra con mayor frecuencia: '{palabra_top}' con {conteo_top} apariciones")
    else:
        print("No se ingresaron palabras válidas.")


if __name__ == "__main__":
    main()