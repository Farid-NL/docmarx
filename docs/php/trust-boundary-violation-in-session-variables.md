---
tags:
  - PHP
  - Baja
---

Suele suceder con las variables superglobales, tales como `$_POST` y `$_GET`, al no ser sanitizadas correctamente.

Envuelve el uso de estas variables con alguna de las siguientes funciones, y su correspondiente
[filtro de saneamiento](https://www.php.net/manual/en/filter.constants.php#constant.filter-unsafe-raw) (1):
{ .annotate }

1.  Evita usar los siguientes filtros, pues resultán en vulnerabilidad _Deprecated Functions_

    - `FILTER_SANITIZE_STRING`
    - `FILTER_SANITIZE_STRIPPED`

<div markdown>

- `#!php filter_input()`
- `#!php filter_var()`

</div>


### `filter_var` :material-star:{ title="Recomendado" }

=== ":material-history: Original"

    ```php
    $_SESSION[$Session]['INDEX_ORIGEN'] = isset($_POST['urlorigen']) ? $_POST['urlorigen'] : '';
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="1"
    /*(1)!*/$_SESSION[$Session]['INDEX_ORIGEN'] = filter_var($_POST['urlorigen'] ?? '', FILTER_SANITIZE_SPECIAL_CHARS);
    ```

    1. Al inferir el tipo de variable _(string)_ de `$_POST['urlorigen']`, se usó el filtro de saneamiento
    `FILTER_SANITIZE_SPECIAL_CHARS`.

### `filter_input`

??? warning "Consideración"

    El contenido de la superglobal que se está filtrando, es el contenido original «en bruto», antes de cualquier
    modificación por parte del usuario.

    Para filtrar una superglobal modificada, utiliza [`filter_var()`](#filter_var) en su lugar.

=== ":material-history: Original"

    ```php
    $nSeleccion = isset($_GET['nSeleccion']) ? $_GET['nSeleccion'] : 0;
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="1"
    /*(1)!*/$nSeleccion = filter_input(INPUT_GET, 'nSeleccion', FILTER_SANITIZE_NUMBER_INT) ?: 0;
    ```

    1. Al inferir el tipo de variable _(int)_ de `$nSeleccion`, se usó el filtro de saneamiento
    `FILTER_SANITIZE_NUMBER_INT`.
