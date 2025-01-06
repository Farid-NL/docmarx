## Solución

Suele suceder con los arreglos asociativos `$_POST` y `$_GET` al no ser sanitizados correctamente.

Agrega envuelve el uso de estos arreglos con la función `#!php htmlspecialchars()` con los siguientes parámetros:

- `#!php ENT_QUOTES`
- `#!php 'UTF-8'`

### Ejemplo

Ubica

=== "Path"
    !!! info "Source"
        **File:** `ClubdeProteccion/index.php`
        <br>
        **Line:** 333
        <br>
        **Object:** strValjson

        **Code snippet:**
        <br>
        ```php linenums="333"
        $strValue .= fgets($strValjson,4096);
        ```

    !!! info "Destination"
        **File:** `ClubdeProteccion/index.php`
        <br>
        **Line:** 519
        <br>
        **Object:** contenido_archivo

        **Code snippet:**
        <br>
        ```php linenums="519"
        echo $contenido_archivo;
        ```

### Código

=== "Original"
    ```php
    if ($strValjson = fopen("$strValjson", "r")) {
        $strValue = '';
        while (!feof($strValjson)) {
            $strValue .= fgets($strValjson, 4096);
        }
        fclose($strValjson);
    }
    ```

=== "Solucionado"
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
