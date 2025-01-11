---
tags:
  - C++
  - Baja
---

Comprueba el resultado de cualquier función llamada que devuelva un valor, y verifica que el resultado sea un valor esperado.

## `remove (stdio. h)`

Envuelve la función en un `#!cpp if` o `#!cpp if-else` y maneja el valor retornado por `remove()` según la lógica de la
aplicación.

=== ":material-history: Original"

    ```cpp
    remove(rutacon);
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```cpp hl_lines="1"
    if (remove(rutacon) != 0) {
        AfxMessageBox("Error al intentar eliminar el archivo de conexion: " + rutacon);
    }
    ```
