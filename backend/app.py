
from flask import Flask, jsonify, request
from conexion import obtener_conexion

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Servidor backend funcionando correctamente",
        "proyecto": "Sistema Distribuido de Gestion de Pedidos"
    })


# CONSULTAR PEDIDOS
@app.route("/pedidos", methods=["GET"])
def listar_pedidos():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, cliente, descripcion, estado
        FROM pedidos
        ORDER BY id
    """)

    pedidos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(pedidos)


# REGISTRAR UN PEDIDO
@app.route("/pedidos", methods=["POST"])
def crear_pedido():
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar los datos del pedido"}), 400

    cliente = datos.get("cliente")
    descripcion = datos.get("descripcion")
    estado = datos.get("estado", "pendiente")

    estados_validos = ["pendiente", "en proceso", "enviado", "entregado"]

    if not cliente or not descripcion:
        return jsonify({"error": "Faltan datos del pedido"}), 400

    if estado not in estados_validos:
        return jsonify({"error": "Estado no valido"}), 400

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO pedidos (cliente, descripcion, estado)
        VALUES (%s, %s, %s)
    """, (cliente, descripcion, estado))

    conexion.commit()
    nuevo_id = cursor.lastrowid

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Pedido registrado correctamente",
        "id": nuevo_id
    }), 201

# ACTUALIZAR UN PEDIDO
@app.route("/pedidos/<int:id>", methods=["PUT"])
def actualizar_pedido(id):
    datos = request.get_json()

    if not datos:
        return jsonify({"error": "Debe enviar los datos para actualizar"}), 400

    cliente = datos.get("cliente")
    descripcion = datos.get("descripcion")
    estado = datos.get("estado")

    estados_validos = ["pendiente", "en proceso", "enviado", "entregado"]

    if not cliente or not descripcion or not estado:
        return jsonify({"error": "Faltan datos del pedido"}), 400

    if estado not in estados_validos:
        return jsonify({"error": "Estado no valido"}), 400

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT estado FROM pedidos WHERE id = %s", (id,))
    pedido = cursor.fetchone()

    if not pedido:
        cursor.close()
        conexion.close()
        return jsonify({"error": "Pedido no encontrado"}), 404

    estado_anterior = pedido["estado"]

    cursor.execute("""
        UPDATE pedidos
        SET cliente = %s, descripcion = %s, estado = %s
        WHERE id = %s
    """, (cliente, descripcion, estado, id))

    if estado_anterior != estado:
        cursor.execute("""
            INSERT INTO historial_pedidos
            (pedido_id, estado_anterior, estado_nuevo)
            VALUES (%s, %s, %s)
        """, (id, estado_anterior, estado))

    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Pedido actualizado correctamente"})

# ELIMINAR UN PEDIDO
@app.route("/pedidos/<int:id>", methods=["DELETE"])
def eliminar_pedido(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM pedidos WHERE id = %s", (id,))
    pedido = cursor.fetchone()

    if not pedido:
        cursor.close()
        conexion.close()
        return jsonify({"error": "Pedido no encontrado"}), 404

    # Eliminar primero el historial relacionado
    cursor.execute(
        "DELETE FROM historial_pedidos WHERE pedido_id = %s",
        (id,)
    )

    # Después eliminar el pedido
    cursor.execute("DELETE FROM pedidos WHERE id = %s", (id,))

    conexion.commit()
    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Pedido eliminado correctamente"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
