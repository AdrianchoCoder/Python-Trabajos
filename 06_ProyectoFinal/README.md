# 🏕️ Glamping Manager – Backend con Flask

Este proyecto implementa el backend de una aplicación web para la gestión de glampings, clientes y reservas. Utiliza **Flask** como framework principal y almacena los datos en archivos **JSON**, sin necesidad de una base de datos relacional.

---

## 📦 Estructura del Proyecto


---

## ⚙️ ¿Cómo funciona el backend?

### 1. `app.py` – Controlador principal

Define todas las rutas de la aplicación Flask:

- `/clientes`, `/glampings`, `/reservas`: muestran listas de cada entidad.
- `/guardar_*`, `/actualizar_*`, `/eliminar_*`: permiten crear, modificar y eliminar datos.
- Usa `render_template` para mostrar vistas y `redirect` para redirigir después de acciones.

---

### 2. `models/` – Lógica de negocio

Cada archivo en esta carpeta representa una entidad del sistema:

#### 🧍 Cliente.py
- Lee y escribe en `clientes.json`.
- Métodos:
  - `guardar()`: crea o actualiza un cliente.
  - `obtener_clientes()`: devuelve todos los clientes.
  - `obtener_cliente_por_id(id)`: busca un cliente específico.
  - `eliminar_cliente_por_id(id)`: elimina un cliente.

#### 🏕️ Glamping.py
- Lee y escribe en `glampings.json`.
- Funciona igual que Cliente, pero con atributos como `capacidad` y `precio_por_noche`.

#### 📅 Reserva.py
- Lee y escribe en `reservas.json`.
- Cada reserva está asociada a un cliente y un glamping.
- Métodos:
  - `guardar()`: guarda o actualiza una reserva.
  - `obtener_reservas(clientes, glampings)`: devuelve reservas con objetos enlazados.
  - `eliminar_reserva_por_id(id)`: elimina una reserva.

---

## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio:

   git clone https://github.com/tu-usuario/glamping-backend.git
   cd glamping-backend
2. Lista de dependencias del Proyecto:
    El requirements.txt, contiene todos los paquetes de Python que estan en el proyecto que se necesitan para funcionar. Es útil porque permite que cualquier persona (o servidor) instale las librerías que utilice para la realizacion del proyecto, con un solo comando.
    pip freeze > requirements.txt
    pip install -r requirements.txt

