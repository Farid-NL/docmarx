---
tags:
  - C++
  - Media
---

Implementa una alternativa segura y recomendada para cualquier función que se haya identificado como peligrosa.

## `strtok`

La función `strtok` se considera insegura porque modifica una cadena y no es thread-safe.

### `strtok_s`

Sustituye `strtok` por `strtok_s` el cual requiere un parámetro `context` adicional para gestionar el estado entre
llamadas.

???+ warning "Consideración en la versión de Visual C++"

    La función `strtok_s` está disponible **a partir** de la versión Visual C++ 2005 (8.0).

    Asegurate de que el proyecto sea compatible, revisa el archivo `.vcproj` por las siguientes lineas:

    ```xml hl_lines="2-3"
    <VisualStudioProject
        ProjectType="Visual C++"
        Version="9.00"
    ```

??? linux "`strtok_r`"

    Si trabajas con algun aplicativo Linux, solo cambia `strtok` por **`strtok_r`**.

    La lógica presentada en el ejemplo se conserva.

=== ":material-history: Original"

    ```cpp
    #include <string.h> // (1)!
    // ...
    char *token = strtok(cServercomple, ",,");

    while (token != NULL) {
        // ...
        token = strtok(NULL, ",,");
    }
    ```

    1. Incluye esta cabecera si es que no está ya incluida en el proyecto.

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```cpp hl_lines="3 4 8"
    #include <string.h> // (1)!
    // ...
    char* context = NULL;
    char *token = strtok_s(cServercomple, ",,", &context);

    while (token != NULL) {
        // ...
        token = strtok_s(NULL, ",,", &context);
    }
    ```

    1. Incluye esta cabecera si es que no está ya incluida en el proyecto.
