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

    - [Windows](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)

      ```shell
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.5.13/install.ps1 | iex"

      # Asegurate de tener "C:\Users\<tu_usuario>\.local\bin" en PATH
      echo $env:Path

      # De no tenerlo en PATH puedes agregarlo de la siguiente forma
      $env:Path = "C:\Users\<tu_usuario>\.local\bin;$env:Path"
      # Los cambios en $env:Path son temporales, funcionando solamente en la sesión activa
      ```

    - [macOS y Linux](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_1)

      ```shell
      curl -LsSf https://astral.sh/uv/0.5.13/install.sh | sh

      # Asegurate de tener "~/.local/bin" en PATH
      echo $PATH

      # De no tenerlo en PATH puede agregarlo de la siguiente forma
      export PATH="~/.local/bin:$PATH"
      # O puedes hacer los cambios permanentes en tu .bashrc o .zshrc
      ```

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
   # Windows CMD
   .\.venv\Scripts\activate.bat
   # Windows Powershell
   Set-ExecutionPolicy RemoteSigned -Scope Process
   .\.venv\Scripts\activate.ps1
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
   # Windows CMD
   .\.venv\Scripts\activate.bat
   # Windows Powershell
   Set-ExecutionPolicy RemoteSigned -Scope Process
   .\.venv\Scripts\activate.ps1
   ```
4. Instala las dependencias.
   ```shell
   python -m pip install -r requirements.txt

   # Si vas a crear algún archivo de python
   python -m pip install -r requirements-dev.txt
   ```

## Desarrollo

### Previsualiza mientras modificas

El servidor reconstruirá automáticamente el sitio al guardarlo. Inícialo con:

```shell
mkdocs serve
```

Luego dirígete a [localhost:8000](http://localhost:8000)

### Agrega una vulnerabilidad

**Documentación del comando**

```text
NAME
       docx-add - Añade una nueva vulnerabilidad a documentar

SYNOPSIS
       docx add [-a | --alta] <language> <vulnerability>
       docx add [-m | --media] <language> <vulnerability>
       docx add [-b | --baja] <language> <vulnerability>

DESCRIPTION
       Crea un archivo markdown en 'docs/<language>' nombrado según la vulnerabilidad en
       kebab-case, además de agregar el nombre de la vulnerabilidad así como la ruta del
       archivo recién creado a la sección nav de mkdocs.yml.

       Dicho archivo se crea con basado en la plantilla vulnerability.tmpl.

       Sólo se puede utilizar una opción a la vez o ninguna, en cuyo caso se dejará la
       etiqueta de severidad comentada.

OPTIONS
       -a, --alta
           Establece la severidad de la vulnerabilidad como alta a través de una etiqueta
           en la cabecera del archivo markdown.

       -m, --media
           Establece la severidad de la vulnerabilidad como media a través de una etiqueta
           en la cabecera del archivo markdown.

       -b, --baja
           Establece la severidad de la vulnerabilidad como baja a través de una etiqueta
           en la cabecera del archivo markdown.
```

**Ejemplo**

 ```shell
 docx add PHP "Insufficient Sanitization for XSS" --baja
 ```

El script se encargará de crear el archivo correspondiente con una plantilla para que documentes rápidamente

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

### Remueve una vulnerabilidad

**Documentación del comando**

```text
NAME
       docx-remove - Remueve una nueva vulnerabilidad

SYNOPSIS
       docx remove <language> <vulnerability>

DESCRIPTION
       Remueve el archivo correspondiente a la vulnerabilidad, además de remover la entrada
       correspondiente a la vulnerabilidad en la sección nav de mkdocs.yml.

       Los argumentos <language> y <vulnerability> deben coincidir exactamente con su
       correspondiente entrada en la sección nav de mkdocs.yml.
```

**Ejemplo**

```shell
docx remove PHP "Insufficient Sanitization for XSS"
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

### Ordena vulnerabilidades

```text
NAME
       docx-sort - Ordena alfabéticamente las vulnerabilidades

SYNOPSIS
       docx sort

DESCRIPTION
       Ordena alfabéticamente las vulnerabilidades y reescribe la sección nav de mkdocs.yml.
```

**Ejemplo**

```shell
docx sort
```

### Linting & Code formating

Si vas a trabajar con archivos python, ya sea al crear o editar un script o un hook, asegúrate de usar los siguientes
comandos durante el desarrollo y al final de cada commit. Esto con la finalidad de mantener el code style consistente.

```shell
# Formatter
ruff format

# Linter
ruff check --fix
```
