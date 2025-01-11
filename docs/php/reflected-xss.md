---
tags:
  - PHP
  - Alta
---

Suele suceder con las variables superglobales, tales como `$_POST` y `$_GET`, al no ser sanitizadas correctamente.

Envuelve el uso de estas variables con la función `#!php htmlspecialchars()` con los siguientes parámetros:

- `#!php ENT_QUOTES`
- `#!php 'UTF-8'`

=== ":material-history: Original"

    ```php
    $_SESSION['token'] = $_POST['token'];
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="1"
    $_SESSION['token'] = htmlspecialchars($_POST['token'], ENT_QUOTES, 'UTF-8');
    ```
