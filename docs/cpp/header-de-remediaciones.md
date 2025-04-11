[Descargar :material-download:](../assets/code/Funciones_vul.h){:download="Funciones_vul.h"}

```cpp
#ifndef FUNCIONES_VUL_H
#define FUNCIONES_VUL_H

class Funciones_vul {
public:
    // Homólogo de la función memcpy
    void *memorycopy(void *dest, const void *src, size_t n) {
        char *p_dest = (char *) dest;
        const char *p_src = (const char *) src;

        for (size_t i = 0; i < n; i++) {
            p_dest[i] = p_src[i];
        }

        return dest;
    }

    // Hómologo de la función memset
    void *llenamemoria(void *b, char c, int len) {
        char *b_char = (char *) b;

        if (b == NULL)
            return NULL;

        while (*b_char && len > 0) {
            *b_char = c;
            b_char++;
            len--;
        }

        return b; // as this pointer has not changed
    }

    // Homólogo de la función sprintf
    int imprimirsprintf(char *str, const char *format, ...) {
        va_list args;
        int count = 0;
        int bufferIndex = 0;

        va_start(args, format);

        while (*format != '\0') {
            if (*format == '%') {
                format++; // avanzar al siguiente carácter después del '%'

                // Procesar los modificadores válidos (solo para este ejemplo)
                if (*format == 'd') {
                    int value = 0;
                    value = va_arg(args, int);
                    char buffer[12]; // suficientemente grande para representar un número entero
                    int numDigits = 0;

                    // Convertir el número entero a una cadena
                    if (value == 0) {
                        buffer[numDigits++] = '0';
                    } else {
                        if (value < 0) {
                            str[bufferIndex++] = '-';
                            value = -value;
                        }

                        while (value != 0) {
                            buffer[numDigits++] = '0' + (value % 10);
                            value /= 10;
                        }

                        // Invertir la cadena para que quede en el orden correcto
                        for (int i = numDigits - 1; i >= 0; i--) {
                            str[bufferIndex++] = buffer[i];
                        }
                    }

                    count += numDigits;
                }
                // Puedes agregar más modificadores como 's', 'c', etc.
            } else if (*format == 's') {
                // Manejar cadenas de caracteres
                const char *svalue = NULL;
                svalue = va_arg(args, const char*);
                while (*svalue != '\0') {
                    str[bufferIndex++] = *svalue++;
                    count++;
                }
            } else {
                str[bufferIndex++] = *format;
                count++;
            }

            format++;
        }

        // str[sizeof(bufferIndex)+2000] = '\0'; // terminar la cadena con un carácter nulo
        // str[bufferIndex] = '\0';

        va_end(args);
        return count;
    }

    // Hómologo de la función strlen
    size_t longuitudlen(const char *str) {
        const char *s = str; // Apuntador auxiliar para recorrer la cadena

        while (*s)
            s++; // Avanza al siguiente carácter contando hasta llegar al final de la cadena

        // Retorna la diferencia de posiciones entre el apuntador final y el inicial, que representa la longitud de la cadena
        return s - str;
    }

    //Homologo de la función strcopy
    char *stringcopy(char *destino, const char *origen) {
        char *ptr = destino;
        while (*origen != '\0') {
            *destino = *origen;
            destino++;
            origen++;
        }
        *destino = '\0';
        return ptr;
    }

    //Homologo de la función atoi
    int caracentero(const char *str) {
        int resultado = 0;
        int signo = 1;
        while (isspace(*str)) {
            str++; // Salta los caracteres de espacio en blanco iniciales
        }
        if (*str == '+' || *str == '-') {
            // Si la cadena comienza con un signo, determina si es positivo o negativo
            if (*str == '-') {
                signo = -1;
            }
            str++; // Salta el signo
        }
        while (isdigit(*str)) {
            // Convierte los dígitos en un número entero
            resultado = resultado * 10 + (*str - '0');
            str++; // Avanza al siguiente caracter de la cadena
        }
        return resultado * signo; // Aplica el signo al resultado final
    }

    //Homologo de la función atol
    long int caralargo(const char *str) {
        long result = 0;
        int sign = 1;

        // Verificar si la cadena comienza con un signo negativo
        if (*str == '-') {
            sign = -1;
            str++;
        }

        // Recorrer la cadena y convertir cada dígito a un valor numérico
        while (*str) {
            if (*str >= '0' && *str <= '9') {
                result = result * 10 + (*str - '0');
            } else {
                // Si se encuentra un caracter no numérico, se detiene la conversión
                break;
            }
            str++;
        }

        // Devolver el resultado con su signo correspondiente
        return sign * result;
    }
};
#endif //FUNCIONES_VUL_H
```
