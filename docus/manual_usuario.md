
# Manual de Usuario
## Sistema Distribuido de Gestión de Pedidos

### 1. Introducción
Este manual explica cómo utilizar el sistema para registrar, consultar, actualizar y eliminar pedidos de clientes.

### 2. Ingreso al sistema
Para ingresar al sistema, el administrador o encargado debe iniciar los servidores y el frontend siguiendo las instrucciones del proyecto.

Después, debe abrir el navegador e ingresar a:

`http://localhost:5173/`

### 3. Pantalla principal
En la pantalla principal se encuentran dos secciones:

- **Registrar nuevo pedido:** permite ingresar el nombre del cliente y la descripción del pedido.
- **Pedidos registrados:** muestra los pedidos almacenados en la base de datos.

### 4. Registrar un pedido
1. Escribir el nombre del cliente.
2. Escribir la descripción del pedido.
3. Hacer clic en el botón "Registrar pedido".
4. El sistema guardará el pedido con el estado inicial "pendiente".

### 5. Consultar pedidos
En la tabla de pedidos registrados se puede consultar el identificador, el cliente, la descripción y el estado de cada pedido.

### 6. Cambiar el estado de un pedido
1. Buscar el pedido que se desea actualizar.
2. Hacer clic en el botón "Cambiar estado".
3. El sistema avanzará al siguiente estado disponible.

Los estados siguen este orden:

- Pendiente.
- En proceso.
- Enviado.
- Entregado.
- Al volver a pulsar, regresa a pendiente.

### 7. Eliminar un pedido
1. Buscar el pedido que se desea eliminar.
2. Hacer clic en el botón "Eliminar".
3. Confirmar la operación en la ventana que aparece.
4. El pedido desaparecerá de la tabla.

### 8. Mensajes del sistema
El sistema muestra mensajes para informar si una operación se realizó correctamente o si ocurrió algún error.

### 9. Recomendaciones
- Verificar los datos antes de registrar un pedido.
- Confirmar que los servidores estén funcionando.
- No cerrar las terminales mientras se utiliza el sistema.
