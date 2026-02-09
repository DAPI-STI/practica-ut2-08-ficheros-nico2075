"""
EX01 (Texto) · Buscar una palabra en un fichero

Objetivo:
- Practicar la lectura de ficheros de texto usando `open(...)`.
- Normalizar el contenido (minúsculas) y contar coincidencias.

Consejo:
- No hace falta una solución "perfecta" de NLP.
  Con que cuentes palabras separadas por espacios y elimines puntuación básica es suficiente.
"""

from __future__ import annotations

from pathlib import Path
import string


def count_word_in_file(path: str | Path, word: str) -> int:
    """
    Devuelve el número de apariciones de `word` dentro del fichero de texto `path`.

    Reglas:
    - Búsqueda NO sensible a mayúsculas/minúsculas.
      Ej: "Hola" cuenta como "hola".
    - Cuenta por palabra (no por subcadena).
      Ej: si word="sol", NO debe contar dentro de "solución".
    - Considera puntuación básica como separador (.,;:!? etc.)
      Pista: puedes traducir la puntuación a espacios.

    Errores:
    - Si el fichero no existe, lanza FileNotFoundError.
    - Si word está vacía o solo espacios, lanza ValueError.

    Ejemplo:
    Fichero: "Hola hola mundo"
    word="hola" -> 2
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"El fichero '{path}' no existe.")
    if not word or word.strip() == "":
        raise ValueError("La palabra a buscar no puede estar vacía ni ser solo espacios.")

    word = word.lower().strip()
    with open(path, encoding="utf-8") as f:
        text = f.read().lower()

    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
    text = text.translate(translator)
    words = text.split()

    return sum(1 for w in words if w == word)