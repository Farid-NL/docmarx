<h1 align="center">
    <br>
    <img src="docs/assets/logo.png" alt="Markdownify" height="100"/>
    <br>
    Docmarx
</h1>

<h4 align="center">Documentación de vulnerabilidades mitigadas (reportadas por <a href="https://checkmarx.com/" target="_blank">Checkmarx</a>).</h4>

[//]: # (<u><h4 align="center"><a href="#" target="_blank">Sitio web</a></h4></u>)

<p align="center">
    <img alt="python-badge" src="https://img.shields.io/badge/python-3.12-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
    <img alt="uv-badge" src="https://img.shields.io/badge/uv-0.5.13-3670A0?style=for-the-badge&logo=uv&logoColor=ffdd54">
</p>

<p align="center">
    <a href="#configuración-uv">Configuración (uv)</a> •
    <a href="#configuración-pip">Configuración (pip)</a> •
    <a href="#desarrollo">Desarrollo</a> •
    <a href="#despliegue">Despliegue</a>
</p>

## Configuración (uv)

1. Instala uv
   - Windows
   - MacOS & Linux
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
   ```

## Desarrollo

## Despliegue
