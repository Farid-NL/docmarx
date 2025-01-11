---
tags:
  - PHP
  - Baja
---

Suele suceder con las variables superglobales, tales como `$_POST` y `$_GET`, al no ser sanitizadas correctamente.
Pero también puede ocurrir con alguna otra variable.

Envuelve el fragmento de código afectado con la función `#!php htmlspecialchars()` con los siguientes parámetros:

- `#!php ENT_QUOTES`
- `#!php 'UTF-8'`

=== ":material-history: Original"

    ```php
    if ($strValjson = fopen("$strValjson", "r")) {
        $strValue = '';
        while (!feof($strValjson)) {
            $strValue .= fgets($strValjson, 4096);
        }
        fclose($strValjson);
    }
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="8"
    if ($strValjson = fopen("$strValjson", "r")) {
        $strValue = '';
        while (!feof($strValjson)) {
            $strValue .= fgets($strValjson, 4096);
        }
        fclose($strValjson);
    }
    $strValue = htmlspecialchars($strValue, ENT_QUOTES, 'UTF-8');
    ```
