# Sistema Distribuido de Gestión de Pedidos

## Descripción

Este proyecto consiste en el desarrollo de un sistema distribuido para gestionar pedidos de clientes. Permite registrar, consultar, actualizar el estado y eliminar pedidos mediante una interfaz web.

El sistema cuenta con dos servidores backend y un balanceador de carga que distribuye las solicitudes y permite utilizar el otro servidor cuando uno deja de estar disponible.

## Tecnologías utilizadas

- Python
- Flask
- MySQL
- React
- JavaScript
- HTML5 y CSS3
- Vite

## Arquitectura del sistema

El proyecto está compuesto por los siguientes elementos:

- **Frontend:** interfaz web desarrollada con React.
- **Servidor backend 1:** procesa solicitudes en el puerto 5000.
- **Servidor backend 2:** procesa solicitudes en el puerto 5001.
- **Balanceador de carga:** recibe las solicitudes en el puerto 8000 y las distribuye entre los dos servidores.
- **Base de datos:** MySQL, utilizada para almacenar los pedidos y su historial de cambios.

## Funcionalidades

- Registrar pedidos.
- Consultar pedidos registrados.
- Actualizar el estado de los pedidos.
- Eliminar pedidos.
- Distribuir solicitudes entre dos servidores backend.
- Continuar atendiendo solicitudes cuando uno de los servidores backend deja de funcionar.

## Estados de los pedidos

- Pendiente.
- En proceso.
- Enviado.
- Entregado.

## Instalación y ejecución

### 1. Requisitos

- Python instalado.
- Node.js y npm instalados.
- MySQL Server instalado.
- Visual Studio Code (recomendado).

### 2. Configurar la base de datos

1. Abrir MySQL Workbench.
2. Ejecutar el archivo `database/gestion_pedidos.sql`.
3. Verificar que se haya creado la base de datos `gestion_pedidos`.

### 3. Configurar la conexión a MySQL

Crear un archivo `.env` en la carpeta principal del proyecto con el siguiente contenido:

```env
DB_PASSWORD=TU_CONTRASEÑA
```

Reemplazar `TU_CONTRASEÑA` por la contraseña del usuario MySQL correspondiente.

### 4. Instalar dependencias de Python

Abrir una terminal en la carpeta principal y ejecutar:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 5. Iniciar los servidores backend

Abrir tres terminales independientes, ubicadas en la carpeta principal del proyecto.

**Terminal 1 - Servidor backend 1:**

```powershell
.\venv\Scripts\Activate.ps1
py backend\app.py
```

**Terminal 2 - Servidor backend 2:**

```powershell
.\venv\Scripts\Activate.ps1
py backend\app_servidor2.py
```

**Terminal 3 - Balanceador de carga:**

```powershell
.\venv\Scripts\Activate.ps1
py backend\balanceador.py
```

### 6. Iniciar el frontend

Abrir una cuarta terminal y ejecutar:

```powershell
cd frontend
npm install
npm run dev
```

### 7. Acceder al sistema

Abrir el navegador e ingresar a:

http://localhost:5173/

### 8. Puertos utilizados

| Componente | Puerto |
|---|---|
| Backend 1 | 5000 |
| Backend 2 | 5001 |
| Balanceador | 8000 |
| Frontend | 5173 |
| MySQL | 3306 |

## Base de datos

El sistema utiliza MySQL y requiere una base de datos llamada `gestion_pedidos`, con las tablas `pedidos`, `servidores` e `historial_pedidos`.

## Tolerancia a fallos

Los dos servidores backend comparten una misma instancia de MySQL. El balanceador permite continuar atendiendo solicitudes cuando uno de los servidores backend deja de responder. La base de datos no cuenta con replicación.

## Autor

Proyecto académico desarrollado para la asignatura de Sistemas Distribuidos.