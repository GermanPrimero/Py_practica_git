# 🐶 git-demo — La Máquina Tonta

El código en sí no importa mucho: es una "máquina" en Python que genera saludos, piropos y datos absurdos. Lo importante es el *flujo* de trabajo.

## ¿Qué hay aquí?

| Archivo | Para qué sirve |
|---|---|
| [`app.py`](app.py) | El código de la máquina tonta |
| [`test_app.py`](test_app.py) | Tests automáticos (pytest) |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | El pipeline: se ejecuta en los servidores de GitHub cada vez que haces push o abres un PR |
| [`EJERCICIO.md`](EJERCICIO.md) | El ejercicio guiado paso a paso (rama → PR → pipeline → merge) |
| [`requirements.txt`](requirements.txt) | Dependencias (solo pytest) |

## 1. Probarlo en local

```bash
cd git-demo
pip install -r requirements.txt
python app.py
```

Y para ejecutar los tests:

```bash
pytest -v
```

Deberían pasar todos en verde ✅ — este es el estado inicial de `main`, antes de hacer el ejercicio.


## 2. Subirlo a tu propio GitHub

Este proyecto ya es un repositorio Git local (rama `main`), pero todavía no está conectado a GitHub. Para practicar Pull Requests necesitas un repo remoto en tu cuenta.

### Opción A: con la web de GitHub
1. Entra en [github.com/new](https://github.com/new) y crea un repositorio vacío llamado `git-demo` (sin README, sin .gitignore – ya lo tenemos).
2. Copia la URL que te da GitHub y ejecútalo aquí:

bash
git remote add origin https://github.com/TU-USUARIO/git-demo.git
git push -u origin main

### Opción B: con GitHub CLI (si lo tienes instalado)

bash
gh repo create git-demo --public --source=. --remote-origin --push

### 3. Hacer el ejercicio

Una vez subido a GitHub, sigue la guía paso a paso de `[EJERCICIO.md](EJERCICIO.md)`: vas a crear una rama, añadir una función nueva, subirla, abrir un Pull Request y ver el pipeline ejecutarse automáticamente en GitHub Actions.

## El flujo de trabajo, en resumen

...

main (rama estable)
    │
    ├── git checkout -b feature/mi-cambio     ← 1. crear rama
    │   │                                    
    │   │   (editar código)
    │   │
    │   ├── git add .                        ← 2. commit
    │   │
    │   └── git commit -m "..."
    │
    ├── git push -u origin feature/mi-cambio ← 3. subir la rama
    │
    ├── Abrir Pull Request en GitHub         ← 4. PR
    │
    ├── GitHub Actions ejecuta el pipeline  ← 5. CI en remoto (automático)
    │   (instala dependencias y corre pytest)
    │
    └── Merge a main cuando esté en verde ✅ ← 6. fusionar

...

## Notas

- La rama `solucion/despedida-tonta` contiene la solución del ejercicio, por si te atascas.
- El pipeline (`.github/workflows/ci.yml`) se dispara con `push` a cualquier rama y con cada `pull_request` contra `main`, así que verás los checks tanto al subir tu rama como dentro del propio PR.