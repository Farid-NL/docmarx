---
tags:
  - Javascript
  - Baja
---

## `load`

Utiliza `$.get` y asegúrate de adaptarlo correctamente.

=== ":material-history: Original"

    ```js
    $dialog.load('consultadatos.php?rfc=' + N + '&folio=' + F + '&serie=' + A).dialog({
        title: 'Consulta de Facturas Electronicas',
        width: 700,
        height: 600,
        modal: true,
        resizable: false,
        autoResize: false,
        draggable: false
    });
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```js hl_lines="1-2 10"
    $.get('consultadatos.php', { rfc: N, folio: F, serie: A }, function(response) {
        $dialog.html(response).dialog({
            title: 'Consulta de Facturas Electronicas',
            width: 700,
            height: 600,
            modal: true,
            resizable: false,
            autoResize: false,
            draggable: false
        });
    });
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado (DOM Purify)"

    ```js hl_lines="1-2 10"
    $.get('consultadatos.php', { rfc: N, folio: F, serie: A }, function(response) {
        $dialog.html(DOMPurify.sanitize(response, {ALLOWED_ATTR: ['cellpadding', 'cellspacing', 'border', 'width', 'height', 'style', 'align', 'colspan', 'BGCOLOR', 'onclick', 'name', 'class']})).dialog({
            title: 'Consulta de Facturas Electronicas',
            width: 700,
            height: 600,
            modal: true,
            resizable: false,
            autoResize: false,
            draggable: false
        });
    });
    ```

## `parseJSON`

Utiliza `JSON.parse` y asegúrate de adaptarlo correctamente.

=== ":material-history: Original"

    ```js
    var json = jQuery.parseJSON(respuesta);
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```js hl_lines="1"
    var json = JSON.parse(respuesta);
    ```
