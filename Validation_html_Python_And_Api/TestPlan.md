Plan de Pruebas - Funciones de Validación

Objetivo:
- Validar enlaces y recursos en un sitio web de comercio electrónico.

Funciones de Validación:

1. Función: validate_link(url)
   - Descripción: Verifica si un enlace responde con un código de estado 200 (OK).
   - Entradas: URL del enlace a validar.
   - Salida: Booleano (verdadero si el enlace es válido, falso si no lo es).

2. Función: get_webpage_content(url)
   - Descripción: Obtiene el contenido HTML de una página web.
   - Entradas: URL de la página web.
   - Salida: Contenido HTML de la página.

3. Función: find_all_src_attributes(html_content)
   - Descripción: Encuentra todos los atributos src en el contenido HTML.
   - Entradas: Contenido HTML de la página.
   - Salida: Lista de enlaces (src) encontrados.

4. Función: construct_full_url(base_url, relative_url)
   - Descripción: Construye una URL completa a partir de una URL base y una URL relativa.
   - Entradas: URL base y URL relativa.
   - Salida: URL completa.

5. Función: validate_all_links_on_page(page_url)
   - Descripción: Valida todos los enlaces en una página web.
   - Entradas: URL de la página web.
   - Salida: Lista de enlaces válidos y no válidos.

6. Función: main()
   - Descripción: Función principal que coordina el proceso de validación.
   - Entradas: Ninguna.
   - Salida: Ninguna.
