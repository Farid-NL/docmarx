---
tags:
  - PHP
  - Media
---

## Solución

Cambia el ciclo `#!php for` por `#!php foreach`

### Ejemplo

=== "Path"
    !!! info "Destination"
        **File:** `ClubdeProteccion/ajax/proc/proc_validaracceso.php`
        <br>
        **Line:** 113
        <br>
        **Object:** response

        **Code snippet:**
        <br>
        ```php linenums="113"
        for($i = 0;$i < sizeof($response->perfil);$i++ ) {
        ```

### Código

=== "Original"
    ```php
    for ($i = 0; $i < sizeof($response->perfil); $i++) {
        if ($response->perfil[$i]->idu_area != $buffer) {
            $buffer = $response->perfil[$i]->idu_area;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas] = new stdClass();
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->idu_area = $response->perfil[$i]->idu_area;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->nom_nombrearea = $response->perfil[$i]->nom_nombrearea;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->ordenmenuarea = $response->perfil[$i]->ordenmenuarea;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->iconoarea = $response->perfil[$i]->iconoarea;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->desc_ayudaarea = $response->perfil[$i]->desc_ayudaarea;

            $totalAreas++;
        }
    }
    ```

=== "Solucionado"
    ```{ .php .annotate hl_lines="1" }
    foreach ($response->perfil as $perfilItem) { // (1)!
        if ($perfilItem->idu_area != $buffer) {
            $buffer = $perfilItem->idu_area;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas] = new stdClass();
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->idu_area = $perfilItem->idu_area;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->nom_nombrearea = $perfilItem->nom_nombrearea;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->ordenmenuarea = $perfilItem->ordenmenuarea;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->iconoarea = $perfilItem->iconoarea;
            $_SESSION['SISTEMAS']['AREA'][$totalAreas]->desc_ayudaarea = $perfilItem->desc_ayudaarea;

            $totalAreas++;
        }
    }
    ```

    1. Asegurate de reemplazar todas las ocurrencias de `$iterable[$i]` por `$item`.
    <br><br>
    En este caso `$response->perfil[$i]`por `$perfilItem`
