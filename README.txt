# Urban Routes - Pruebas Automatizadas

## Descripcion del Proyecto

Este proyecto contiene pruebas automatizadas para la aplicacion Urban Routes, un servicio de solicitud de taxis. Las pruebas verifican el flujo completo de pedido de un taxi, incluyendo:

- Configuracion de direccion de origen y destino
- Seleccion de tarifa Comfort
- Registro de numero de telefono con verificacion OTP
- Agregado de tarjeta de credito
- Mensaje para el conductor
- Solicitud de manta y panuelos
- Pedido de helados
- Confirmacion de solicitud de taxi

## Tecnologias y Tecnicas Utilizadas

### Tecnologias
- Python 3.14+ - Lenguaje de programacion
- Selenium WebDriver - Automatizacion de navegadores
- pytest - Framework de pruebas
- ChromeDriver - Driver para navegador Chrome

### Tecnicas
- Page Object Model (POM) - Patron de diseno para organizar localizadores y metodos
- Getters, Setters, Clickers, Readers - Estructura de metodos para interactuar con elementos
- JavaScript Executor - Para interactuar con elementos React y evitar excepciones
- WebDriverWait - Esperas explicitas para elementos dinamicos
- Pruebas independientes - Cada prueba se ejecuta de forma aislada

## Estructura del Proyecto

qa-project-Urban-Routes-es/
├── data/
│   ├── __init__.py
│   └── data.py              # Datos de prueba (URL, direcciones, numeros, tarjetas)
├── helpers/
│   ├── __init__.py
│   └── utilities.py         # Funciones auxiliares (retrieve_phone_code)
├── pages/
│   ├── __init__.py
│   └── urban_routes_page.py # Page Object con localizadores y metodos
├── tests/
│   ├── __init__.py
│   └── test_urban_routes.py # Pruebas automatizadas
├── main.py                  # Ejecutor de pruebas
└── README.md                # Este archivo

## Requisitos Previos

Antes de ejecutar las pruebas, asegurate de tener instalado:

1. Python 3.14 o superior
2. Google Chrome (ultima version)
3. ChromeDriver (compatible con tu version de Chrome)

### Instalacion de Dependencias

pip install selenium pytest

### Configuracion de ChromeDriver

Asegurate de que ChromeDriver este en tu PATH o en el directorio del proyecto.

## Ejecucion de Pruebas

### Ejecutar todas las pruebas

python main.py

### Ejecutar una prueba especifica

pytest tests/test_urban_routes.py::TestUrbanRoutes::test_set_route -v

### Ejecutar con mas detalles

pytest tests/test_urban_routes.py -v

### Ver resultados con reporte

pytest tests/test_urban_routes.py -v --tb=short

## Descripcion de las Pruebas

| Prueba | Descripcion |
|--------|-------------|
| test_set_route | Configura direccion de origen y destino |
| test_select_comfort_tariff | Selecciona la tarifa Comfort |
| test_fill_phone_number | Registra numero de telefono con verificacion OTP |
| test_add_credit_card | Agrega tarjeta de credito |
| test_add_message_for_driver | Escribe mensaje para el conductor |
| test_request_blanket_and_tissues | Solicita manta y panuelos |
| test_order_ice_creams | Pide 2 helados |
| test_request_taxi_final | Confirma la solicitud de taxi |
| test_wait_for_driver_info | Espera informacion del conductor (opcional) |

## Datos de Prueba

Los datos de prueba se encuentran en data/data.py:

urban_routes_url = 'https://...'  # URL del servidor de pruebas
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number = '1234 4321 1408'
card_code = '111'
message_for_driver = 'Muestrame el camino al museo'

## Notas Adicionales

- El proyecto utiliza retrieve_phone_code() para interceptar el codigo de confirmacion enviado por la aplicacion
- Los campos de tarjeta (CVV) son manejados con JavaScript para interactuar correctamente con React
- Las pruebas estan disenadas para ejecutarse de forma independiente

## Autor

Johanna-80

## Licencia

Este proyecto es parte del curso de automatizacion de pruebas de TripleTen.