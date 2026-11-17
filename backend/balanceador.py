from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Direcciones de los servidores backend
servidores = [
    "http://127.0.0.1:5000",
    "http://127.0.0.1:5001"
]

# Control de distribución
servidor_actual = 0


@app.route("/pedidos", methods=["GET", "POST"])
@app.route("/pedidos/<int:id>", methods=["PUT", "DELETE"])
def balancear_pedidos(id=None):

    global servidor_actual

    # Intentar utilizar los dos servidores
    for intento in range(len(servidores)):

        indice = (servidor_actual + intento) % len(servidores)
        servidor = servidores[indice]

        try:
            if id is None:
                url = servidor + "/pedidos"
            else:
                url = servidor + "/pedidos/" + str(id)

            respuesta = requests.request(
                method=request.method,
                url=url,
                json=request.get_json(silent=True),
                timeout=3
            )

            servidor_actual = (indice + 1) % len(servidores)

            return (
                respuesta.content,
                respuesta.status_code,
                {"Content-Type": respuesta.headers.get(
                    "Content-Type", "application/json"
                )}
            )

        except requests.exceptions.RequestException:
            continue

    return jsonify({
        "error": "Ningun servidor backend esta disponible"
    }), 503


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)