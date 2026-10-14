"""Tests de La Máquina Tonta.

Se ejecutan automáticamente:
    - en local, con: pytest -v
    - en remoto, por el pipeline de GitHub Actions cada vez que haces
      push o abres un Pull Request (ver .github/workflows/ci.yml)
"""

import pytest

from app import saludar, piropear, edad_de_perro


def test_saludar_incluye_el_nombre():
    resultado = saludar("Alex")
    assert "Alex" in resultado


def test_saludar_con_nombre_vacio_usa_desconocido():
    resultado = saludar("")
    assert "desconocido" in resultado


def test_piropear_incluye_el_nombre():
    resultado = piropear("Alex")
    assert "Alex" in resultado


def test_edad_de_perro_multiplica_por_siete():
    assert edad_de_perro(3) == 21


def test_edad_de_perro_con_cero():
    assert edad_de_perro(0) == 0

def test_edad_de_perro_negativa_lanza_error():
    with pytest.raises(ValueError):
        edad_de_perro(-1)

# EJERCICIO: cuando añadas la función despedir(nombre) en app.py
# añade aqui su test siguiendo el mismo patrón que los de arriba

