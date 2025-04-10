---
tags:
  - Javascript
  - Baja
---

> La librería [DOM Purify](https://github.com/cure53/DOMPurify) parece no hacer efecto en esta vulnerabilidad.

Suele suceder porque Checkmarx detecta `.value` como un valor potencialmente contaminado.

Evita usar `value` al generar una URL que será utilizada por `#!js window.location.href(...)` o `#!js window.open(...)`

## Alternativa 1

!!! warning "Consideración"
    **Solo** usarlo si el valor del elemento HTML está predeterminado y no cambiará durante la ejecución del programa.

Reemplaza `value` por `getAttribute('value')`

=== ":material-history: Original"

    ```js
    huellahe(DOMPurify.sanitize(document.getElementById('user').value));
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```js hl_lines="1"
    var userElement = document.getElementById('user').getAttribute('value');
    huellahe(DOMPurify.sanitize(userElement));
    ```

---

## Alternativa 2

!!! warning "Posiblemente genere errores"
    Al guardar el elemento HTML entero en vez de solo su valor, puede generar errores

Reemplaza `#!js document.getElementById('...').value` por `#!js document.querySelector('#...')`

=== ":material-history: Original"

    ```js
    var variables ="empleado=" + document.getElementById('usuario').value +
        "&delcentro=" + document.getElementById('txt_delcentro').value +
        "&alcentro=" +document.getElementById('txt_alcentro').value +
        "&fechacorte=" + fechacortebuffer +
        "&empresa=" +document.getElementById('cbx_empresa').value;
    opciones = "top=15,left=15,width=700,height=800,toolbar=no,menubar=no,status=yes,scrollbars=yes,resizable=no;"
    var ventmp = window.open("../proc/proc_exporta_excel.php?" + variables, 'ventmp', opciones);
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```js hl_lines="1-5"
    var variables ="empleado=" + document.querySelector('#usuario') +
        "&delcentro=" + document.querySelector('#txt_delcentro') +
        "&alcentro=" +document.querySelector('#txt_alcentro') +
        "&fechacorte=" + fechacortebuffer +
        "&empresa=" +document.querySelector('#cbx_empresa');
    opciones = "top=15,left=15,width=700,height=800,toolbar=no,menubar=no,status=yes,scrollbars=yes,resizable=no;"
    var ventmp = window.open("../proc/proc_exporta_excel.php?" + variables, 'ventmp', opciones);
    ```
