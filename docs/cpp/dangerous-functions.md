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

1. Crea un [header](../assets/code/Funciones_vul.h){:download="Funciones_vul.h" title="Descargar header"} en la [raíz del
   proyecto]{title="Ejemplo"} que contendrá funciones homólogas a funciones con vulnerabilidades. En este caso `memcpy`
2. Instancía la clase `Funciones_vul` y reemplaza `memcpy` por ^^**`memorycopy`**^^ en el archivo afectado con la
   vulnerabilidad.

[raíz del proyecto]: header-de-remediaciones.md/#como-usarlo

=== ":material-history: Original"

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

    ```cpp hl_lines="3 7 9-10"
    #define MAIN
    //...
    #include "Funciones_vul.h"

    int SN0015( char *cInput1, char *cInput2 )
    {
        Funciones_vul vul;
        //...
        vul.memorycopy( &parametroEntrada1, cInput1, sizeof( EstructurasElp ) );
        vul.memorycopy( &parametroEntrada2, cInput2, sizeof( EstructurasElp ) );
        //...
    }
    ```

## `sprintf`

1. Crea un [header](../assets/code/Funciones_vul.h){:download="Funciones_vul.h" title="Descargar header"} en la [raíz del
   proyecto]{title="Ejemplo"} que contendrá funciones homólogas a funciones con vulnerabilidades. En este caso `sprintf`
2. Instancía la clase `Funciones_vul` y reemplaza `sprintf` por ^^**`imprimirsprintf`**^^ en el archivo afectado con la
   vulnerabilidad.

[raíz del proyecto]: header-de-remediaciones.md/#como-usarlo

=== ":material-history: Original"

    ```cpp
    //...


    BOOL CDlgGenerarliquidaciones::OnInitDialog()
    {

        //...
        sprintf(cTexto,"Error en "+ sqlTxt);
        //...
    }
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```cpp hl_lines="2 6 8"
    //...
    #include "Funciones_vul.h"

    BOOL CDlgGenerarliquidaciones::OnInitDialog()
    {
        Funciones_vul vul;
        //...
        vul.imprimirsprintf(cTexto,"Error en "+ sqlTxt);
        //...
    }
    ```

## `atoi`

1. Crea un [header](../assets/code/Funciones_vul.h){:download="Funciones_vul.h" title="Descargar header"} en la [raíz del
   proyecto]{title="Ejemplo"} que contendrá funciones homólogas a funciones con vulnerabilidades. En este caso `atoi`
2. Instancía la clase `Funciones_vul` y reemplaza `atoi` por ^^**`caracentero`**^^ en el archivo afectado con la
   vulnerabilidad.

[raíz del proyecto]: header-de-remediaciones.md/#como-usarlo

=== ":material-history: Original"

    ```cpp
    #define MAIN

    //...

    int SN0047(char *cInput1,char *cInput2)
    {

        //...
        iOpcion = atoi(EstElpGralDllEnt1.opcion);
        //...
    }
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```cpp hl_lines="2 7 9"
    #define MAIN
    #include "Funciones_vul.h"
    //...

    int SN0047(char *cInput1,char *cInput2)
    {
        Funciones_vul vul;
        //...
        iOpcion = vul.caracentero(EstElpGralDllEnt1.opcion);
        //...
    }
    ```
