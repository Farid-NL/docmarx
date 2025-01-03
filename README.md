<h1 align="center">
    <br>
    <img src="docs/assets/logo.png" alt="Markdownify" height="100"/>
    <br>
    Docmarx
</h1>

<h4 align="center">Documentación de vulnerabilidades mitigadas reportadas por <a href="https://checkmarx.com/" target="_blank">Checkmarx</a>.</h4>

<p align="center">
    <img alt="python-badge" src="https://img.shields.io/badge/python-3.12-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img alt="uv-badge" src="https://img.shields.io/badge/uv-0.5.13-3670A0?style=for-the-badge&logo=uv&logoColor=ffdd54">
</p>

<p align="center">
    <a href="#configuración-uv">Configuración (uv)</a> •
    <a href="#configuración-pip">Configuración (pip)</a> •
    <a href="#desarrollo">Desarrollo</a>
</p>

## Configuración (uv)

1. Instala uv
   - Standalone Installer
      - [Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)
      - [MacOS & Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)
   - [Winget (Windows)](https://docs.astral.sh/uv/getting-started/installation/#winget)
   - [GitHub Releases (Windows, MacOS & Linux)](https://github.com/astral-sh/uv/releases)
2. Utiliza la versión de python correcta: `>= 3.12`. Si es necesario instálala por medio del sig. comando:
   ```shell
   uv python install 3.12
   ```
3. Clona el repositorio y ubícate en el directorio.
   ```shell
   git clone <url>
   cd <direcotorio>
   ```
4. Crea y activa el ambiente virtual
   ```shell
   uv venv --python 3.12

   # MacOS & Linux
   source .venv/bin/activate
   # Windows
   activate
   ```
5. Instala las dependencias.
   ```shell
   uv sync
   ```

## Configuración (pip)
> - El comando `python` o `python3` es usado en MacOS & Linux
> - El comando `py` es usado en Windows

1. Asegurate de utilizar la versión de python correcta: `>= 3.12`.
2. Clona el repositorio y ubícate en el directorio.
   ```shell
   git clone <url>
   cd <direcotorio>
   ```
3. Crea y activa el ambiente virtual
   ```shell
   python -m venv .venv

   # MacOS & Linux
   source .venv/bin/activate
   # Windows
   activate
   ```
4. Instala las dependencias.
   ```shell
   python -m pip -r requirements.txt
   python -m pip -r requirements-dev.txt
   ```

## Desarrollo

Se tiene disponible un script llamado **docx** que facilita la documentación de vulnerabilidades.

### Agregar una vulnerabilidad

- uv + venv activo
   ```shell
   #docx add <lenguaje-de-programación> <vulnerabilidad>
   docx add PHP "Insufficient Sanitization for XSS"
   ```
- pip + venv activo
   ```shell
   #python ./scripts/docx.py add <lenguaje-de-programación> <vulnerabilidad>
   python ./scripts/docx.py add PHP "Insufficient Sanitization for XSS"
   ```

El script se encargará de crear el archivo correspondiente

```diff
 docs/
 ├── assets
 │   └── logo.png
 ├── index.md
+├── php
+│   └── insufficient-sanitization-for-xss.md
 └── stylesheets
     └── extra.css
```

Además de añadir la referencia correspondiente en mkdocs.yml

```diff
 nav:
   - Inicio: index.md
+  - PHP:
+      - Insufficient Sanitization for XSS: php/insufficient-sanitization-for-xss.md
```

### Remover una vulnerabilidad

- uv + venv activo
   ```shell
   #docx remove <lenguaje-de-programación> <vulnerabilidad>
   docx remove PHP "Insufficient Sanitization for XSS"
   docx remove Python "Communication Over HTTP"
   ```
- pip + venv activo
   ```shell
   #python ./scripts/docx.py remove <lenguaje-de-programación> <vulnerabilidad>
   python ./scripts/docx.py remove PHP "Insufficient Sanitization for XSS"
   python ./scripts/docx.py remove Python "Communication Over HTTP"
   ```

El script se encargará de remover el archivo correspondiente

```diff
 docs/
 ├── assets
 │   └── logo.png
 ├── index.md
 ├── php
-│   └── insufficient-sanitization-for-xss.md
 └── stylesheets
     └── extra.css
```

Además de remover la referencia correspondiente en mkdocs.yml

```diff
 nav:
   - Inicio: index.md
-  - PHP:
-      - Client DOM Stored XSS: php/client-dom-stored-xss.md
+  - PHP: []
```
