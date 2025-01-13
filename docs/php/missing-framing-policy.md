---
tags:
  - PHP
  - Baja
---

Establece la cabecera `X-FRAME-OPTIONS` con el valor `SAMEORIGIN`.

=== ":material-history: Original"

    ```php
    <?php
    //...
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="3"
    <?php
    //...
    header('X-Frame-Options: SAMEORIGIN');
    //...
    ```
