# Proyecto Urban Grocers 

# Proyecto de Testing de API - Usuarios y Kits

Este proyecto realiza pruebas automatizadas sobre una API REST que permite la creación de usuarios y la creación de kits personales asociados a dichos usuarios.

## 🧪 Tecnologías utilizadas

- **Python 3.12+**
- **pytest**: framework principal para ejecución de pruebas
- **requests**: para realizar llamadas HTTP a la API
- **pytest.mark.parametrize**: para parametrización de entradas

## 📁 Estructura del proyecto

```
.
├── configuration.py # Configuración de rutas y endpoints
├── data.py # Datos base reutilizables para las pruebas
├── sender_stand_request.py # Funciones auxiliares para enviar solicitudes HTTP
└── create_kit_name_kit_test.py # Pruebas relacionadas con la creación de kits
```

## ✅ Pruebas implementadas

Las pruebas se centran en el endpoint de creación de kits de la aplicación Urban Grocers, validando tanto casos válidos como inválidos.

### 🔐 Flujo de prueba general

Cada prueba sigue los siguientes pasos:

1. Autenticación de un usuario y obtención del `authToken`.
2. Creación del encabezado `Authorization` con el token.
3. Envío de la solicitud `POST /kits` con diferentes variaciones del campo `"name"`.
4. Validación del código de respuesta y el contenido del body.

---

### ✅ Casos positivos (espera `201 Created`)

| n° | Descripción                           | Entrada             |
|----|---------------------------------------|---------------------|
| 1  | Longitud mínima de `name` (1 char)    | `"name": "a"`       |
| 2  | Longitud máxima permitida (511 chars) | `"name": "A"*511`   |
| 3  | Caracteres especiales                 | `"name": "№%@,"`    |
| 4  | Nombre con espacios                   | `"name": " A Aaa "` |
| 5  | Números en el nombre                  | `"name": "123"`     |

---

### ❌ Casos negativos (espera `400 Bad Request`)

| Nº | Descripción                                | Entrada           |
|----|--------------------------------------------|-------------------|
| 1  | Cadena vacía                               | `"name": ""`      |
| 2  | Longitud mayor a la permitida (512 chars)  | `"name": "A"*512` |
| 3  | Tipo incorrecto (`int` en vez de `str`)    | `"name": 123`     |
| 4  | Omisión del campo `"name"` en la solicitud | `kit_body = {}`   |

---

## ▶️ Ejecución de pruebas

Asegúrate de tener instaladas las dependencias:

```bash
  pip install pytest requests
```

y ejecuta:

```bash
  pytest -v
```