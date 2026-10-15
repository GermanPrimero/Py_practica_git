"""
🤪 La Máquina Tonta 🤪

Un generador de saludos, piropos y datos absurdos, sin ninguna
utilidad real más que servir de excusa para practicar Git y GitHub.

Este proyecto se usa para practicar:
    - crear una rama (branch)
    - hacer commits
    - abrir un Pull Request (PR)
    - ver un pipeline (GitHub Actions) ejecutarse solo

Mira el README.md y el EJERCICIO.md para la guía paso a paso.
"""

import random

SALUDOS = [
    "¡Ey, {nombre}, qué alegría verte por aquí!",
    "¡{nombre}! Justo la persona que quería ver (creo).",
    "Saludos cordiales, {nombre}. El café ya está listo.",
]

CUMPLIDOS = [
    "{nombre}, tienes el don de encontrar aparcamiento siempre.",
    "{nombre}, tu capacidad para hacer nudos en los cables es asombrosa.",
    "{nombre}, brillas más que la pantalla del móvil a las 3 de la mañana.",
]


def saludar(nombre: str) -> str:
    """Devuelve un saludo tonto y aleatorio para `nombre`."""
    if not nombre:
        nombre = "desconocido"
    plantilla = random.choice(SALUDOS)
    return plantilla.format(nombre=nombre)

def piropear(nombre: str) -> str:
    """Devuelve un piropo absurdo para `nombre`."""
    if not nombre:
        nombre = "desconocido"
    plantilla = random.choice(CUMPLIDOS)
    return plantilla.format(nombre=nombre)


def edad_de_perro(anios_humanos: int) -> int:
    """Convierte años humanos en 'años de perro' (x7), de forma muy poco científica."""
    if anios_humanos < 0:
        raise ValueError("No se puede tener una edad negativa, ¡ni los perros!")
    return anios_humanos * 7


# 👉 EJERCICIO: aquí falta una función `despedir(nombre)`.
# Sigue las instrucciones de EJERCICIO.md para añadirla en tu propia rama.
def despedir(nombre: str) -> str:
    if not nombre:
        nombre = "desconocido"
    return f"Adios, {nombre} Que los semaforos siempre esten a tu favor"


def menu() -> None:
    """Punto de entrada de la CLI: pide un nombre y muestra saludo + piropo."""
    nombre = input("¿Cómo te llamas? ")
    print(saludar(nombre))
    print(piropear(nombre))
    print(f"En años de perro, 30 años son {edad_de_perro(30)} años de perro.")
    print(despedir(nombre))


if __name__ == "__main__":
    menu()