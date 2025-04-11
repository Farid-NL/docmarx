---
tags:
  - C++
  - Alta
---

Evita usar `#!cpp sizeof()` con apuntadores

A continuación se muestra soluciones específicas.

## `CargarDLL`

=== ":material-history: Original"

    === ":simple-cplusplus: CargarDLL.cpp"

        ```cpp
        CargarDLL::CargarDLL(
            char *cDLLCompleteFileName, char *cProjectName,
            char *cLocalInput1, char *cLocalInput2,
            char *cLocalOutput1,
            char *cLocalOutput2 )
        {
            //...
            if ( hDLL != NULL )
            {
                functPointer = ( LPFN2 )GetProcAddress( hDLL, cProjectName );

                if ( !functPointer )
                {
                    //...
                }
                else
                {
                    //..
                    memcpy( sOutput1, cLocalOutput1, sizeof( cLocalOutput1 ) );
                    memcpy( sOutput2, cLocalOutput2, sizeof( cLocalOutput2 ) );
                }
            }
            //...
        }
        ```

    === ":simple-cplusplus: CargarDLL.h"

        ```cpp
        #ifndef __CARGAR_DLL_H__
        #define __CARGAR_DLL_H__

        class CargarDLL
        {
        public:

            CargarDLL( char *cDLLCompleteFileName, char *cProjectName, char *cLocalInput1, char *cLocalInput2 );
            CargarDLL(
                char *cDLLCompleteFileName, char *cProjectName,
                char *cLocalInput1, char *cLocalInput2,
                char *cLocalOutput1,
                char *cLocalOutput2 );
            ~CargarDLL();

            //...
        };


        #endif __CARGAR_DLL_H__
        ```

    === ":material-alert: Archivos impactados"

        ```cpp
        CargarDLL cargar("CONTA65.DLL","CONTA65",
            cParamEntrada1,cParamEntrada2,
            cParamSalida1,
            cParamSalida2);
        ```


=== ":material-checkbox-marked-circle-outline: Solucionado"

    === ":simple-cplusplus: CargarDLL.cpp"

        ```cpp hl_lines="4-5 19-20"
        CargarDLL::CargarDLL(
            char *cDLLCompleteFileName, char *cProjectName,
            char *cLocalInput1, char *cLocalInput2,
            char *cLocalOutput1, const size_t cLocalOutput1Size,
            char *cLocalOutput2, const size_t cLocalOutput2Size )
        {
            //...
            if ( hDLL != NULL )
            {
                functPointer = ( LPFN2 )GetProcAddress( hDLL, cProjectName );

                if ( !functPointer )
                {
                    //...
                }
                else
                {
                    //..
                    memcpy( sOutput1, cLocalOutput1, cLocalOutput1Size );
                    memcpy( sOutput2, cLocalOutput2, cLocalOutput2Size );
                }
            }
            //...
        }
        ```

    === ":simple-cplusplus: CargarDLL.h"

        ```cpp hl_lines="12-13"
        #ifndef __CARGAR_DLL_H__
        #define __CARGAR_DLL_H__

        class CargarDLL
        {
        public:

            CargarDLL( char *cDLLCompleteFileName, char *cProjectName, char *cLocalInput1, char *cLocalInput2 );
            CargarDLL(
                char *cDLLCompleteFileName, char *cProjectName,
                char *cLocalInput1, char *cLocalInput2,
                char *cLocalOutput1, size_t cLocalOutput1Size,
                char *cLocalOutput2, size_t cLocalOutput2Size );
            ~CargarDLL();

            //...
        };


        #endif __CARGAR_DLL_H__
        ```

    === ":material-check-decagram: Archivos impactados"

        ```cpp hl_lines="3-4"
        CargarDLL cargar("CONTA65.DLL","CONTA65",
            cParamEntrada1,cParamEntrada2,
            cParamSalida1, sizeof(cParamSalida1)
            cParamSalida2, sizeof(cParamSalida2));
        ```
