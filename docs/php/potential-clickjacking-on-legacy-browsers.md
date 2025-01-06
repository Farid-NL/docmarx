## Solución

Agrega el [fragmento de código](#código) arriba del todo del archivo, afuera de la etiqueta `<?php`.

O en algún lado entre el código HTML

### Ejemplo

Explicación del ejemplo

=== "Path"
    !!! info "Destination"
        **File:** `ClubdeProteccion/ajax/proc/proc_excelmovimientocovid.php`
        <br>
        **Line:** 1
        <br>
        **Object:** CxJSNS_7aed654e

        **Code snippet:**
        <br>
        ```text linenums="1"
        <?php
        ```

### Código

=== "Original"
    ```js+php
    <?php
    ```

=== "Solucionado"
    ```js+php hl_lines="1-13"
    <style id = "antiClickjack"> body {display:none !important;} </style>
    <script type="text/javascript">
        if(self === top)
        {
            var antiClickjack = document.getElementById("antiClickjack");
            antiClickjack.parentNode.removeChild(antiClickjack);
        }
        else
        {
            var _location = 'self.location';
            window['top.location'] = window[_location];
        }
    </script>

    <?php
    ```
