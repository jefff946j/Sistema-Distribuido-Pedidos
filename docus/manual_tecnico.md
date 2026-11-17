
# Manual Técnico
## Sistema Distribuido de Gestión de Pedidos

### 1. Introducción
Este documento describe la estructura técnica y el funcionamiento del sistema distribuido de gestión de pedidos, desarrollado para administrar pedidos de clientes mediante una arquitectura cliente-servidor.

### 2. Arquitectura del sistema
El sistema está compuesto por los siguientes elementos:

- **Frontend:** desarrollado con React, JavaScript, HTML5 y CSS3. Permite al usuario interactuar con el sistema.
- **Backend 1:** desarrollado con Python y Flask. Atiende solicitudes a través del puerto 5000.
- **Backend 2:** desarrollado con Python y Flask. Atiende solicitudes a través del puerto 5001.
- **Balanceador de carga:** desarrollado con Flask y Requests. Recibe las solicitudes por el puerto 8000 y las distribuye entre los servidores backend.
- **Base de datos:** MySQL. Almacena los pedidos, los servidores registrados y el historial de cambios.

### 3. Tecnologías utilizadas
- Python.
- Flask.
- MySQL.
- React.
- JavaScript.
- HTML5.
- CSS3.
- Vite.
- MySQL Connector.
- Requests.

### 4. Estructura del proyecto
- `backend/`: contiene los servidores, el balanceador y la conexión a MySQL.
- `frontend/`: contiene la interfaz web.
- `database/`: contiene el archivo SQL para crear la base de datos.
- `docs/`: contiene los manuales del proyecto.
- `venv/`: contiene el entorno virtual de Python.

### 5. Funcionamiento del sistema
El usuario realiza operaciones desde la interfaz web. Las solicitudes pasan por el balanceador de carga, que las envía a uno de los dos servidores backend.

Los servidores procesan las solicitudes y se conectan a MySQL para consultar o modificar la información.

Si uno de los servidores backend no está disponible, el balanceador intenta utilizar el otro servidor.

### 6. Servicios disponibles
| Método | Ruta | Función |
|---|---|---|
| GET | /pedidos | Consultar pedidos |
| POST | /pedidos | Registrar un pedido |
| PUT | /pedidos/{id} | Actualizar un pedido |
| DELETE | /pedidos/{id} | Eliminar un pedido |

### 7. Base de datos
La base de datos se llama `gestion_pedidos` y contiene tres tablas:

- `pedidos`: almacena la información de los pedidos.
- `servidores`: registra los servidores backend.
- `historial_pedidos`: almacena los cambios de estado de los pedidos.

### 8. Tolerancia a fallos
El sistema utiliza un balanceador de carga que distribuye las solicitudes entre dos servidores backend. Cuando uno deja de responder, se intenta enviar la solicitud al otro.

Los dos servidores utilizan la misma instancia de MySQL. Por lo tanto, la tolerancia a fallos implementada corresponde a la capa backend y no contempla la caída del servidor de base de datos.

### 9. Seguridad
La contraseña de MySQL se almacena en un archivo `.env`, que está excluido del repositorio mediante `.gitignore`.
