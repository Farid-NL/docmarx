## Solución

Suele suceder con los arreglos asociativos `$_POST` y `$_GET` al no ser sanitizados correctamente.

Agrega envuelve el uso de estos arreglos con la función `#!php htmlspecialchars()` con los siguientes parámetros:

- `#!php ENT_QUOTES`
- `#!php 'UTF-8'`


### Ejemplo

=== "Path 4"
    !!! info "Destination"
        **File:** `ClubdeProteccion/index.php`
        <br>
        **Line:** 519
        <br>
        **Object:** contenido_archivo

    !!! info "Code snippet"
        ```php
        $_SESSION['token'] = $_POST['token'];
        ```

### Código

=== "Original"
    ```php
    $_SESSION['token'] = $_POST['token'];
    ```
=== "Solucionado"
    ```php hl_lines="1"
    $_SESSION['token'] = htmlspecialchars($_POST['token'], ENT_QUOTES, 'UTF-8');
    ```
