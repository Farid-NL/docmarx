---
tags:
  - C++
  - Baja
---

Implementa una alternativa segura y recomendada para cualquier función que se haya identificado como peligrosa.

## `memset`

1. Crea un [header](../assets/code/Funciones_vul.h){:download="Funciones_vul.h" title="Descargar header"} en la raíz del
   proyecto que contendrá [funciones homólogas a funciones con vulnerabilidades]. En este caso `memset`
2. Incluye el header en el archivo afectado con la vulnerabilidad.
3. Instancía la clase `Funciones_vul`
4. Utiliza la instancia para reemplazar `memset` por `llenamemoria`

[funciones homólogas a funciones con vulnerabilidades]: header-de-remediaciones.md

=== ":material-history: Original"

    === ":material-file-tree: Estructura del proyecto"

        ```
        sn0015/
        ├── Clases
        │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.cpp
        │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.hpp
        │   ├── ...
        ├── DlgCompararCifrasQuincena.cpp
        ├── DlgCompararCifrasQuincena.h
        ├── ggn.lib
        ├── ModuloPrincipal.cpp
        └── ...
        ```

    === ":simple-cplusplus: Código"

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

    === ":material-file-tree: Estructura del proyecto"

        ```diff
         sn0015/
         ├── Clases
         │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.cpp
         │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.hpp
         │   ├── ...
         ├── DlgCompararCifrasQuincena.cpp
         ├── DlgCompararCifrasQuincena.h
        +├── Funciones_vul.h
         ├── ggn.lib
         ├── ModuloPrincipal.cpp
         └── ...
        ```

    === ":simple-cplusplus: Código"

        ```cpp hl_lines="2 7 9-10"
        #define MAIN
        #include "Funciones_vul.h"
        //...

        int SN0015( char *cInput1, char *cInput2 )
        {
            Funciones_vul vul;
            //...
            vul.llenamemoria( &parametroEntrada1, 0, sizeof( EstructurasElp ) );
	        vul.llenamemoria( &parametroEntrada2, 0, sizeof( EstructurasElp ) );
            //...
        }
        ```
