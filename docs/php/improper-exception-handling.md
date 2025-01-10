---
tags:
  - PHP
  - Baja
---

## Solución

En el caso de `#!php json_encode` y `#!php json_decode` se usa la la bandera `JSON_THROW_ON_ERROR` como argumento y se
envuelve la sentencia en un bloque `#!php try-catch`.

### `json_encode`

=== "Original"

    ```php
    echo json_encode($respuesta);
    ```

=== "Solucionado"

    ```php hl_lines="1 3-5"
    try {
        echo json_encode($respuesta, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        echo "Ocurrió un error al intentar generar el archivo.";
    }
    ```

---

### `json_decode`

#### `PHP >= 8.0`

=== "Original"

    ```php
    echo json_encode($respuesta);
    ```

=== "Solucionado"

    ```{ .php .annotate hl_lines="1 3-5" }
    try {
        echo json_encode($respuesta, flags: JSON_THROW_ON_ERROR); // (1)!
    } catch (JsonException $e) {
        echo "Ocurrió un error al intentar generar el archivo.";
    }
    ```

    1. Haciendo uso de [Named Arguments](https://www.php.net/manual/en/functions.arguments.php#functions.named-arguments)

#### `PHP < 8.0`

=== "Original"

    ```php
    echo json_encode($respuesta);
    ```

=== "Solucionado"

    ```{ .php .annotate hl_lines="1 3-5" }
    try {
        echo json_encode($respuesta, null, 512, JSON_THROW_ON_ERROR); // (1)!
    } catch (JsonException $e) {
        echo "Ocurrió un error al intentar generar el archivo.";
    }
    ```

    1. Colocando los valores por default de cada argumento hasta llegar al que nos interesa: `flags`, el último.
