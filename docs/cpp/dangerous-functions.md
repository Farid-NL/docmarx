---
tags:
  - C++
  - Media
---

Implementa una alternativa segura y recomendada para cualquier función que se haya identificado como peligrosa.

## `strtok`

Reemplaza `strtok` por `strtok_s` el cual requiere un parámetro `context` adicional para gestionar el estado entre
llamadas.

???+ warning "Consideración en la versión de Visual C++"

    La función `strtok_s` está disponible **a partir** de la versión Visual C++ 2005 (8.0).

    Asegurate de que el proyecto sea compatible, revisa el archivo `.vcproj` por las siguientes lineas:

    ```xml hl_lines="2-3"
    <VisualStudioProject
        ProjectType="Visual C++"
        Version="9.00"
    ```

??? linux "`strtok_r`"

    Si trabajas con algun aplicativo Linux, solo cambia `strtok` por **`strtok_r`**.

    La lógica presentada en el ejemplo se conserva.

=== ":material-history: Original"

    ```cpp
    #include <string.h> // (1)!
    // ...
    char *token = strtok(cServercomple, ",,");

    while (token != NULL) {
        // ...
        token = strtok(NULL, ",,");
    }
    ```

    1. Incluye esta cabecera si es que no está ya incluida en el proyecto.

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```cpp hl_lines="3 4 8"
    #include <string.h> // (1)!
    // ...
    char* context = NULL;
    char *token = strtok_s(cServercomple, ",,", &context);

    while (token != NULL) {
        // ...
        token = strtok_s(NULL, ",,", &context);
    }
    ```

    1. Incluye esta cabecera si es que no está ya incluida en el proyecto.

## `memcpy`

1. Crea un [header](../assets/code/Funciones_vul.h){:download="Funciones_vul.h" title="Descargar header"} en la raíz del
   proyecto que contendrá [funciones homólogas a funciones con vulnerabilidades]. En este caso `memcpy`
2. Instancía la clase `Funciones_vul` y reemplaza `memcpy` por `memorycopy` en el archivo afectado con la
   vulnerabilidad.

[funciones homólogas a funciones con vulnerabilidades]: header-de-remediaciones.md

=== ":material-history: Original"

    === ":material-file-tree: Estructura del proyecto"

        ```
        sn0015/
        ├── Clases/
        │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.cpp
        │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.hpp
        │   └── ...
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
            memcpy( &parametroEntrada1, cInput1, sizeof( EstructurasElp ) );
            memcpy( &parametroEntrada2, cInput2, sizeof( EstructurasElp ) );
            //...
        }
        ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    === ":material-file-tree: Estructura del proyecto"

        ```diff
         sn0015/
         ├── Clases/
         │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.cpp
         │   ├── CSapConsultarCifrasDeControlPOSGRESQL01.hpp
         │   └── ...
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
            vul.memorycopy( &parametroEntrada1, cInput1, sizeof( EstructurasElp ) );
            vul.memorycopy( &parametroEntrada2, cInput2, sizeof( EstructurasElp ) );
            //...
        }
        ```
