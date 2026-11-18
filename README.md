# Urban Routes | Automatización de interfaz con Selenium

Scripts de prueba para el flujo de solicitud de taxi en Urban Routes, organizados con Python, pytest y Page Object Model.

## Resumen

Automatizo acciones sobre formularios y ventanas del flujo de reserva. Durante el desarrollo identifiqué elementos HTML, preparé localizadores y organicé las interacciones en un Page Object.

## Alcance

El archivo [`tests/test_urban_routes.py`](tests/test_urban_routes.py) contiene **nueve métodos de prueba**: dirección, tarifa Comfort, teléfono, tarjeta, mensaje para el conductor, extras, helados, solicitud final y visualización de datos del conductor.

## Herramientas

`Python` · `Selenium WebDriver` · `pytest` · `Chrome` · `Page Object Model`

## Cómo ejecutar o revisar

Instala Python, Google Chrome y las dependencias. La URL de la aplicación está en [`data/data.py`](data/data.py): **puede estar caducada y necesita un entorno de pruebas activo**.

```bash
git clone https://github.com/Johanna-80/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es
python -m pip install selenium pytest
python -m pytest tests/test_urban_routes.py -v
```

También es posible usar `python main.py`. El código usa ChromeDriver; comprueba que el controlador sea compatible con Chrome.

## Evidencias y resultados

- [Nueve métodos definidos](tests/test_urban_routes.py) y [localizadores y acciones](pages/urban_routes_page.py).
- El flujo incluye aserciones sobre direcciones y confirmación de solicitud.
- **No hay un reporte reciente de ejecución publicado**; no se atribuye porcentaje de aprobación ni reducción de tiempo.

## Estructura

```text
main.py                        # Ejecuta pytest
data/data.py                   # URL temporal y datos de prueba
pages/urban_routes_page.py    # Page Object
helpers/utilities.py          # Funciones auxiliares
tests/test_urban_routes.py     # Nueve métodos de prueba
```

## Limitaciones

Las pruebas de esta clase recorren etapas de un mismo flujo y comparten una sesión de navegador; **no deben describirse como independientes**. Algunas interacciones dependen de ventanas dinámicas o datos de un entorno temporal. Antes de repetir la ejecución hay que confirmar la URL, el navegador y los datos de prueba.

## Próximos pasos

- Confirmar la versión de Python y Chrome con la que se ejecute actualmente.
- Añadir registro de ejecución, capturas y revisar el aislamiento de los casos.
- Mantener el repositorio sin cachés de Python ni archivos de configuración personal.

---
**Johanna Vásquez** · [Portafolio web](https://johanna-80.github.io/) · [Perfil GitHub](https://github.com/Johanna-80)
