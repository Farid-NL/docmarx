---
tags:
  - C++
  - Media
---

Implementa una alternativa segura y recomendada para cualquier función que se haya identificado como peligrosa.

## `CDynLinkLibrary`

=== ":material-history: Original"

    ```cpp
    new CDynLinkLibrary(SN0015DLL);
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```cpp hl_lines="1"
    static CDynLinkLibrary dynDLL(SN0015DLL);
    ```
