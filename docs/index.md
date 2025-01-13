# Docmarx

Documentación de vulnerabilidades mitigadas reportadas por Checkmarx.

## Como contribuir

Crea un pull request a través de Github.

### Code style: Pyhon :material-language-python:

Asegúrate de haber instalado las dependencias de desarrollo y ejecuta los siguientes comandos ^^durante^^ el desarrollo y
^^antes^^ de cada commit.

```shell
ruff format
ruff check --fix
```

### Code style: Markdown :material-language-markdown:

Asegúrate de separar cada elemento markdown entre saltos de línea, incluyendo elementos anidados.

```shell hl_lines="2 4 6 10"
??? note "Una nota importante" # (1)!

    === "Tab 1" # (2)!

        **Código importante:**

        ```php # (3)!
        // ...
        ```

        Más información...
```

1. [Leyenda](#leyendas)
2. Leyenda :material-arrow-right-thin: [Pestañas de contenido](#pestanas-de-contenido)
3. Leyenda :material-arrow-right-thin: Pestañas de contenido :material-arrow-right-thin: [Bloque de código](#bloques-de-codigo)

## Markdown en el proyecto

### :material-code-json: Bloques de código [:material-link:](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#usage "Material for MkDocs")

````text title="Bloque de código"
``` py
import tensorflow as tf
```
````

<div class="result" markdown>

```py
import tensorflow as tf
```

</div>

=== "Resaltado de líneas individuales"

    ```` markdown title="Bloque de código con lineas resaltadas"
    ``` py hl_lines="2 4"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```
    ````

    <div class="result" markdown>

    ``` py linenums="1" hl_lines="2 4"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

    </div>

=== "Resaltado de rango de líneas"

    ```` markdown title="Bloque de código con rango de lineas resaltadas"
    ``` py hl_lines="3-5"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```
    ````

    <div class="result" markdown>

    ``` py hl_lines="3-5"
    def bubble_sort(items):
        for i in range(len(items)):
            for j in range(len(items) - 1 - i):
                if items[j] > items[j + 1]:
                    items[j], items[j + 1] = items[j + 1], items[j]
    ```

    </div>

### :material-tab: Pestañas de contenido [:material-link:](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage "Material for MkDocs")

``` title="Pestañas de contenido con bloques de código"
=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```
```

<div class="result" markdown>

=== "C"

    ``` c
    #include <stdio.h>

    int main(void) {
      printf("Hello world!\n");
      return 0;
    }
    ```

=== "C++"

    ``` c++
    #include <iostream>

    int main(void) {
      std::cout << "Hello world!" << std::endl;
      return 0;
    }
    ```

</div>

### :material-alert-outline: Leyendas [:material-link:](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#usage "Material for MkDocs")

```text title="Leyenda"
!!! note "Nota"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

<div class="result" markdown>

!!! note "Nota"

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

</div>

### :material-plus-circle: Anotaciones [:material-link:](https://squidfunk.github.io/mkdocs-material/reference/annotations/#usage "Material for MkDocs")

Las anotaciones de código pueden colocarse en cualquier lugar de un bloque de código donde pueda colocarse un comentario
para el lenguaje del bloque, por ejemplo, para JavaScript en `// ...` y `/* ... */`, para YAML en `# ...`, etc.

```` title="Anotoaciones en bloques de código"
``` .c++
#include <iostream> // (1)!

int main(void) {
  std::cout << "Hello world!" << std::endl;
  return 0;
}
```

1. Incluye esta librería
````

<div class="result" markdown>

``` .c++
#include <iostream> // (1)!

int main(void) {
  std::cout << "Hello world!" << std::endl;
  return 0;
}
```

1. Incluye esta librería

</div>

### :material-emoticon-happy-outline: Iconos más usados [:material-link:](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#usage "Material for MkDocs")


- `:material-history:` :material-history:
- `:material-checkbox-marked-circle-outline` :material-checkbox-marked-circle-outline:
- `:material-arrow-right-thin:` :material-arrow-right-thin:
- `:octicons-light-bulb-24:` :octicons-light-bulb-24:
- `:material-star:` :material-star:
- `:material-file-tree:` :material-file-tree:

