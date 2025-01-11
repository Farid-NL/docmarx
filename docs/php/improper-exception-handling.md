---
tags:
  - PHP
  - Baja
---

Envuelve la sentencia afectada en un bloque `#!php try-catch`.

## `json_encode`

=== ":material-history: Original"

    ```php
    echo json_encode($respuesta);
    ```

=== ":material-checkbox-marked-circle-outline:  Solucionado"

    === "`PHP < 7.3`"

        ```php hl_lines="3"
        try {
            echo json_encode($respuesta);
        } catch (\Throwable $th) {
            // echo "Ocurrió un error al intentar generar el archivo.";
        }
        ```

    === "`PHP >= 7.3`"

        ```php hl_lines="2 3"
        try {
            echo json_encode($respuesta, JSON_THROW_ON_ERROR);
        } catch (JsonException $e) {
            // echo "Ocurrió un error al intentar generar el archivo.";
        }
        ```

## `json_decode`

=== ":material-history: Original"

    ```php
    echo json_decode($respuesta);
    ```

=== ":material-checkbox-marked-circle-outline:  Solucionado"

    === "`PHP < 7.3`"

        ```php hl_lines="3"
        try {
            echo json_decode($respuesta);
        } catch (\Throwable $th) {
            // echo "Ocurrió un error al intentar generar el archivo.";
        }
        ```

    === "`PHP >= 7.3, < 8.0`"

        ```{ .php .annotate hl_lines="2 3" }
        try {
            echo json_decode($respuesta, null, 512, JSON_THROW_ON_ERROR); // (1)!
        } catch (JsonException $e) {
            // echo "Ocurrió un error al intentar generar el archivo.";
        }
        ```

        1. Coloca los valores predeterminados de cada argumento hasta llegar al que interesa: `flags`, el último.

    === "`PHP >= 8.0`"

        ```{ .php .annotate hl_lines="2 3" }
        try {
            echo json_decode($respuesta, flags: JSON_THROW_ON_ERROR); // (1)!
        } catch (JsonException $e) {
            // echo "Ocurrió un error al intentar generar el archivo.";
        }
        ```

        1. Haciendo uso de [Named Arguments](https://www.php.net/manual/en/functions.arguments.php#functions.named-arguments)
