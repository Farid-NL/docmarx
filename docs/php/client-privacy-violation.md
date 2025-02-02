---
tags:
  - PHP
  - Media
---

Suele suceder porque Checkmarx detecta palabras potencialmente inseguras, tales como `password`, `clave`, `contraseña`,
etc.

^^**Cambia**^^ esas palabras por palabras equivalentes:

- `clave` :material-arrow-right-thin: `clv`
- `password` :material-arrow-right-thin: `pswd`
- `password` :material-arrow-right-thin: `pa55word`

Asegúrate de rastrear todos sus usos y el origen de este tipo de palabras, y cambia todas.

## :octicons-light-bulb-24: Ejemplo

??? checkmarx "Reporte de Checkmarx"

    === "Source"

        **File:** `files/js/frm_agregarpropuestasueldosADMON.js`
        <br>
        **Line:** 3132
        <br>
        **Object:** clave

        **Code snippet:**

        ```html+php linenums="3132"
        option += "<option style='text-align: left;' value='" + json.datos[i].clave + "'>" + json.datos[i].clave + ' - ' + json.datos[i].nombre + "</option>";
        ```

    === "Destination"

        **File:** `files/js/frm_agregarpropuestasueldosADMON.js`
        <br>
        **Line:** 3136
        <br>
        **Object:** html

        **Code snippet:**

        ```html+php linenums="3136"
        $("#cbo_rot_seccion").trigger("chosen:updated").html(option);
        ```

Checkmarx detecta la palabra `clave` el origen de la vulnerabilidad. Cambiamos dicho valor por `clv`, en el archivo.

=== ":material-history: Original"

    ```js hl_lines="11"
    $.ajax({
        // ...
        url: 'ajax/json/json_fun_obtener_filtros_rotacion.php' // (1)!
    })
        .done(function(data) {
            json = json_decode(data);
            if (json.estado == 0) {
                // ...
                for (var i = 0; i < json.datos.length; i++) {
                    option += "<option style='text-align: left;' value='"
                        + json.datos[i].clave + "'>" + json.datos[i].clave
                        + ' - ' + json.datos[i].nombre + "</option>";
                }
                $("#cbo_rot_seccion").trigger("chosen:updated").html(option);
                $("#cbo_rot_seccion").trigger("chosen:updated");
            }
            // ...
        })
        // ...
    ```

    1. La solicitud HTTP utiliza esta URL, siendo éste archivo el origen de `clave`.

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```js hl_lines="11"
    $.ajax({
        // ...
        url: 'ajax/json/json_fun_obtener_filtros_rotacion.php' // (1)!
    })
        .done(function(data) {
            json = json_decode(data);
            if (json.estado == 0) {
                // ...
                for (var i = 0; i < json.datos.length; i++) {
                    option += "<option style='text-align: left;' value='"
                        + json.datos[i].clv + "'>" + json.datos[i].clv
                        + ' - ' + json.datos[i].nombre + "</option>";
                }
                $("#cbo_rot_seccion").trigger("chosen:updated").html(option);
                $("#cbo_rot_seccion").trigger("chosen:updated");
            }
            // ...
        })
        // ...
    ```

    1. La solicitud HTTP utiliza esta URL, siendo éste archivo el origen de `clave`.

También es necesario modificar el archivo `json_fun_obtener_filtros_rotacion.php`, pues es el archivo que
genera el JSON consumido por `frm_agregarpropuestasueldosADMON.js`.

=== ":material-history: Original"

    ```php hl_lines="4"
    foreach ($ds as $value) {
        $arr[] = array('nombre' => trim($value['snombre']),
            'value' => $value['iid'],
            'clave' => $value['sclave']
        );
    }
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="4"
    foreach ($ds as $value) {
        $arr[] = array('nombre' => trim($value['snombre']),
            'value' => $value['iid'],
            'clv' => $value['sclave']
        );
    }
    ```
