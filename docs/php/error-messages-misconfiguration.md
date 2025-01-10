---
tags:
  - PHP
  - Baja
---

## Solución

Desactiva las directivas relacionadas con mostrar errores por medio de la **creación** de un archivo `.ini` en la ^^raíz
del proyecto^^:

```{.ini .annotate title="php.ini"}
display_startup_errors = Off
display_errors = Off
error_reporting = 0
; (1)!
```

1. Es aconsejable activar las siguientes directivas
```ini linenums="4"
log_errors = On
error_log = /ruta/a/tu/error.log
```

=== "Original"

    ```text title="Estructura del proyecto"
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

=== "Solucionado"

    ```diff title="Estructura del proyecto"
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
