---
tags:
  - PHP
  - Baja
---

Sanitiza las variables usando una de estas formas:

- [Reflected XSS](reflected-xss.md)
- [Trust Boundary Violation in Session Variables](trust-boundary-violation-in-session-variables.md)

=== ":material-history: Original"

    ```php
    $iIdu_tiposeguro = $_POST['iIdu_tiposeguro']) ?: 0;
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="1"
    $iIdu_tiposeguro = filter_input(INPUT_POST, 'iIdu_tiposeguro', FILTER_SANITIZE_NUMBER_INT) ?: 0;
    ```
