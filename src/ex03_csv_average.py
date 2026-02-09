"""
EX03 (CSV) · Calcular la media de una columna

Objetivo:
- Leer un CSV con cabecera (primera línea).
- Usar la librería estándar `csv` (recomendado: csv.DictReader).
- Convertir datos a float y calcular una media.

Ejemplo típico:
- Un CSV de calificaciones con columnas: name, average
"""

from __future__ import annotations

from pathlib import Path
import csv

def csv_average(path: str | Path, column: str) -> float:
    """
    Calcula y devuelve la media de la columna numérica `column` en el CSV `path`.

    Reglas:
    - El CSV tiene cabecera.
    - `column` debe existir en la cabecera. Si no, ValueError.
    - Todos los valores de esa columna deben poder convertirse a float. Si no, ValueError.
    - Si no hay filas de datos (CSV vacío tras la cabecera), ValueError.
    - Si el fichero no existe, FileNotFoundError.

    Ejemplo:
    name,average
    Ana,10
    Luis,6

    csv_average(..., "average") -> 8.0
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"El fichero '{path}' no existe.")
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if column not in reader.fieldnames:
            raise ValueError(f"La columna '{column}' no existe en el CSV.")
        values = []
        for row in reader:
            try:
                values.append(float(row[column]))
            except (ValueError, TypeError):
                raise ValueError(f"Valor no numérico en la columna '{column}'.")
        if not values:
            raise ValueError("El CSV no contiene datos tras la cabecera.")
        return sum(values) / len(values)