---
tags:
  - Javascript
  - Alta
---

Sanitiza el valor correspondiente con ayuda de [DOM Purify](https://github.com/cure53/DOMPurify).

En algunos casos, en los que solo es esté insertando texto plano, se puede utilizar `.text()`.

## DOM Purify

!!! note "Nota"
    En función del programa puede que sea necesario permitir ciertos atributos, etiquetas, etc.

    Revisa la [documentación de DOM Purify] y el siguiente [ejemplo].

    [documentación de DOM Purify]: https://github.com/cure53/DOMPurify?tab=readme-ov-file#control-our-allow-lists-and-block-lists
    [ejemplo]: client-jquery-deprecated-symbols.md/#__tabbed_1_3

=== ":material-history: Original"

    ```js
    $("#cbx_sistema").html(select);
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```js hl_lines="1"
    $("#cbx_sistema").html(DOMPurify.sanitize(select));
    ```
