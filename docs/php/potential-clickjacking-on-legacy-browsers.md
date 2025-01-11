---
tags:
  - PHP
  - Baja
---

Agrega el [fragmento de código](#__tabbed_1_2) arriba del todo del archivo, afuera de la etiqueta `<?php`.

=== ":material-history: Original"

    ```js+php
    <?php
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

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
