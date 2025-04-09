---
tags:
  - PHP
  - Baja
---

Cambia la función por una equivalente soportada.

## `utf8_encode`

=== ":material-history: Original"

    ```php
    echo utf8_encode($respuesta);
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="1"
    echo mb_convert_encoding($respuesta, 'UTF-8', 'ISO-8859-1');
    ```

## `utf8_decode`

=== ":material-history: Original"

    ```php
    echo utf8_decode($respuesta);
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="1"
    echo mb_convert_encoding($respuesta, 'ISO-8859-1', 'UTF-8');
    ```
