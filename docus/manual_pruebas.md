
# Manual de Pruebas
## Sistema Distribuido de Gestión de Pedidos

### 1. Objetivo
Documentar las pruebas realizadas para comprobar el funcionamiento del sistema distribuido, sus operaciones principales y la tolerancia a fallos de los servidores backend.

### 2. Pruebas funcionales

| Prueba | Procedimiento | Resultado esperado |
|---|---|---|
| Consultar pedidos | Ingresar al sistema | Mostrar los pedidos registrados |
| Registrar pedido | Completar los campos y pulsar Registrar | Guardar el pedido en MySQL |
| Actualizar pedido | Pulsar Cambiar estado | Avanzar al siguiente estado |
| Eliminar pedido | Pulsar Eliminar y confirmar | Eliminar el pedido |
| Consultar mediante el balanceador | Enviar una solicitud a través del puerto 8000 | Recibir la información de los pedidos |

### 3. Prueba de los dos servidores
**Procedimiento:**
1. Iniciar el servidor backend 1 en el puerto 5000.
2. Iniciar el servidor backend 2 en el puerto 5001.
3. Iniciar el balanceador en el puerto 8000.
4. Consultar los pedidos a través del balanceador.

**Resultado:** los dos servidores respondieron correctamente y permitieron consultar la información almacenada en MySQL.

### 4. Prueba de tolerancia a fallos
**Procedimiento:**
1. Iniciar los dos servidores backend y el balanceador.
2. Detener el servidor backend 1.
3. Realizar una consulta a través del balanceador.
4. Comprobar que el sistema intenta utilizar el servidor backend 2.

**Resultado:** el sistema continuó respondiendo mediante el segundo servidor backend.

### 5. Prueba de persistencia
**Procedimiento:**
1. Registrar un pedido desde la interfaz.
2. Consultar los pedidos.
3. Reiniciar o cambiar el servidor backend utilizado.
4. Consultar nuevamente los pedidos.

**Resultado:** el pedido permaneció almacenado porque ambos servidores utilizan la misma base de datos MySQL.

### 6. Conclusión
Las pruebas permitieron comprobar las operaciones principales del sistema, la comunicación entre frontend y backend, el almacenamiento de información en MySQL y la continuidad del servicio cuando uno de los servidores backend deja de responder.
