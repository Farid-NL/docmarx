---
tags:
  - C++
  - Baja
---

Implementa una alternativa segura y recomendada para cualquier función que se haya identificado como peligrosa.

## `memset`

1. Crea un [header](../assets/code/Funciones_vul.h){:download="Funciones_vul.h" title="Descargar header"} en la [raíz del
   proyecto]{title="Ejemplo"} que contendrá funciones homólogas a funciones con vulnerabilidades. En este caso `memset`
2. Instancía la clase `Funciones_vul` y reemplaza `memset` por ^^**`llenamemoria`**^^ en el archivo afectado con la
   vulnerabilidad.

[raíz del proyecto]: header-de-remediaciones.md/#como-usarlo

=== ":material-history: Original"

    ```cpp
    #define MAIN
    //...


    int SN0015( char *cInput1, char *cInput2 )
    {

        //...
        memset( &parametroEntrada1, 0, sizeof( EstructurasElp ) );
        memset( &parametroEntrada2, 0, sizeof( EstructurasElp ) );
        //...
    }
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```cpp hl_lines="3 7 9-10"
    #define MAIN
    //...
    #include "Funciones_vul.h"

    int SN0015( char *cInput1, char *cInput2 )
    {
        Funciones_vul vul;
        //...
        vul.llenamemoria( &parametroEntrada1, 0, sizeof( EstructurasElp ) );
        vul.llenamemoria( &parametroEntrada2, 0, sizeof( EstructurasElp ) );
        //...
    }
    ```
