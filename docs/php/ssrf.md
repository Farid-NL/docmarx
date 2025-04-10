---
tags:
  - PHP
  - Media
---

Suele suceder con las variables superglobales, tales como `$_POST` y `$_GET`, al no ser sanitizadas correctamente.

Envuelve el uso de estas variables con alguna de las siguientes funciones, y su correspondiente
[filtro de saneamiento](https://www.php.net/manual/en/filter.constants.php#constant.filter-unsafe-raw) (1):
{ .annotate }

1.  Evita usar los siguientes filtros, pues resultán en vulnerabilidad _Deprecated Functions_

    - `FILTER_SANITIZE_STRING`
    - `FILTER_SANITIZE_STRIPPED`

<div class="annotate" markdown>

- `#!php filter_var()` (1)
- `#!php htmlspecialchars()` (2)

</div>

1.  Úsalo principalmente para valores `int` y `float`

    Consulta otros ejemplos [aquí](trust-boundary-violation-in-session-variables.md)

2.  Úsalo principalmente para valores `string`

    Consulta otros ejemplos [aquí](reflected-xss.md)

=== ":material-history: Original"

    ```php
    $numRegion = $_POST['numRegion'] ?? 0;

    $urlServlet = $_POST['urlServlet'] ?? '';
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="1 3"
    $numRegion = filter_var($_POST['numRegion'] ?? 0, FILTER_SANITIZE_NUMBER_INT);

    $urlServlet = htmlspecialchars($_POST['urlServlet'] ?? '', ENT_QUOTES, 'UTF-8');
    ```
