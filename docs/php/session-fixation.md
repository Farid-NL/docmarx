---
tags:
  - PHP
  - Media
---

Agrega `#!php session_destroy()` en donde corresponda según lo reportado en la sección de _Destination_ del reporte de
Checkmarx y su correspondiente fragmento de código.

=== ":material-history: Original"

    ```html+php
    function errorhandler($input) {
        echo "<script language='javascript'>window.location.href='$urlIntranet';</script>";
        exit(0);
    }
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```html+php hl_lines="3"
    function errorhandler($input) {
        echo "<script language='javascript'>window.location.href='$urlIntranet';</script>";
        session_destroy();
        exit(0);
    }
    ```
