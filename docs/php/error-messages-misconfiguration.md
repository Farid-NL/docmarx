---
tags:
  - PHP
  - Baja
---

Desactiva las directivas relacionadas con mostrar errores por medio de la **creación** de un archivo `.ini` en la ^^raíz
del proyecto^^:

=== ":material-history: Original"

    ```title="Estructura del proyecto"
    ClubdeProteccion/
    ├── ajax/
    │   ├── frm/
    │   ├── json/
    │   └── proc/
    ├── files/
    ├── clubdeProteccion.php
    ├── index.php
    └── log14-04-2024_proc_validaracceso_intranet.txt
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    === ":material-file-tree: Estructura del proyecto"

        ```diff
         ClubdeProteccion/
         ├── ajax/
         │   ├── frm/
         │   ├── json/
         │   └── proc/
         ├── files/
         ├── clubdeProteccion.php
         ├── index.php
         ├── log14-04-2024_proc_validaracceso_intranet.txt
        +└── php.ini
        ```

    === ":material-file-cog: php.ini"

        ```ini
        display_startup_errors = Off
        display_errors = Off
        error_reporting = 0
        ; (1)!
        ```

        1. Es aconsejable activar las siguientes directivas
        ```ini
        log_errors = On
        error_log = /ruta/a/tu/log_de_errores.log
        ```
