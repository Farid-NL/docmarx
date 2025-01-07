---
tags:
  - PHP
  - Media
---

## Solución

Con base a lo reportado en la sección de _Destination_ del reporte de Checkmarx y su correspondiente fragmento de código,
agrega `#!php session_destroy()` en donde corresponda.

### Ejemplo

Comparando las ocurrencias del archivo `ClubdeProteccion/index.php`, queda claro que la
función `#!php errorhandler($e);` es la raíz del problema, por lo que la solución se añade a esta.

=== "Path A"
    !!! info "Destination"
        **File:** `ClubdeProteccion/index.php`
        <br>
        **Line:** 225
        <br>
        **Object:** ExprStmt

        **Code snippet:**
        <br>
        ```php linenums="225"
        if (isset($jresponse["error"])) errorhandler($jresponse["error_description"]);
        ```

=== "Path B"
    !!! info "Destination"
        **File:** `ClubdeProteccion/index.php`
        <br>
        **Line:** 220
        <br>
        **Object:** ExprStmt

        **Code snippet:**
        <br>
        ```php linenums="220"
        errorhandler($e);
        ```

### Código

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
