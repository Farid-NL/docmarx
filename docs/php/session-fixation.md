---
tags:
  - PHP
  - Media
---

## Solución

Con base a lo reportado en la sección de _Destination_ del reporte de Checkmarx y su correspondiente fragmento de código,
agrega `#!php session_destroy()` en donde corresponda.

=== "Original"
    ```html+php
    function errorhandler($input) {
        echo "<script language='javascript'>window.location.href='$urlIntranet';</script>";
        exit(0);
    }
    ```

=== "Solucionado"
    ```html+php hl_lines="3"
    function errorhandler($input) {
        echo "<script language='javascript'>window.location.href='$urlIntranet';</script>";
        session_destroy();
        exit(0);
    }
    ```
