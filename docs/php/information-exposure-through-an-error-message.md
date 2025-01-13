---
tags:
  - PHP
  - Baja
---

Cambia el manejo de excepciones/errores usando `#!php error_log`.

=== ":material-history: Original"

    ```php
    } catch (Exception $ex) {
        $mensaje = "";
        $mensaje = $ex->getMessage();
        $estado = -2;
    }
    ```

=== ":material-checkbox-marked-circle-outline: Solucionado"

    ```php hl_lines="2 4-5"
    } catch (Exception $ex) {
        $mensaje = "Ocurrió un error en la Base de Datos. Revisa el log '_proc_ce_buscar_empleado.txt'";
        $estado = -2;
        error_log(date("g:i:s a") . " -> Error al consumir proc_buscar_empleado_cecc\n", 3, "../log" . date('d-m-Y') . "_proc_ce_buscar_empleado.txt");
        error_log("\t\t" . "   -> Error: $estado; Tipo: " . $ex->getMessage() . "  \n", 3, "../log" . date('d-m-Y') . "_proc_ce_buscar_empleado.txt");
    }
    ```
