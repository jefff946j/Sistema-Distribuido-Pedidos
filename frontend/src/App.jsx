
import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [pedidos, setPedidos] = useState([])
  const [cliente, setCliente] = useState('')
  const [descripcion, setDescripcion] = useState('')
  const [mensaje, setMensaje] = useState('')

  const cargarPedidos = async () => {
    try {
      const respuesta = await fetch('/api/pedidos')
      const datos = await respuesta.json()
      setPedidos(datos)
    } catch (error) {
      setMensaje('No se pudo conectar con el servidor')
    }
  }

  useEffect(() => {
    cargarPedidos()
  }, [])

  const agregarPedido = async (e) => {
    e.preventDefault()

    try {
      const respuesta = await fetch('/api/pedidos', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          cliente,
          descripcion,
          estado: 'pendiente'
        })
      })

      const datos = await respuesta.json()

      if (!respuesta.ok) {
        setMensaje(datos.error || 'No se pudo registrar el pedido')
        return
      }

      setCliente('')
      setDescripcion('')
      setMensaje('Pedido registrado correctamente')
      cargarPedidos()
    } catch (error) {
      setMensaje('Error al registrar el pedido')
    }
  }

  const cambiarEstado = async (pedido) => {
    const estados = ['pendiente', 'en proceso', 'enviado', 'entregado']
    const indice = estados.indexOf(pedido.estado)
    const nuevoEstado = estados[(indice + 1) % estados.length]

    try {
      const respuesta = await fetch(`/api/pedidos/${pedido.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          cliente: pedido.cliente,
          descripcion: pedido.descripcion,
          estado: nuevoEstado
        })
      })

      const datos = await respuesta.json()

      if (!respuesta.ok) {
        setMensaje(datos.error || 'No se pudo actualizar el pedido')
        return
      }

      setMensaje('Estado actualizado correctamente')
      cargarPedidos()
    } catch (error) {
      setMensaje('Error al actualizar el pedido')
    }
  }

  const eliminarPedido = async (id) => {
    if (!window.confirm('¿Deseas eliminar este pedido?')) return

    try {
      const respuesta = await fetch(`/api/pedidos/${id}`, {
        method: 'DELETE'
      })

      const datos = await respuesta.json()

      if (!respuesta.ok) {
        setMensaje(datos.error || 'No se pudo eliminar el pedido')
        return
      }

      setMensaje('Pedido eliminado correctamente')
      cargarPedidos()
    } catch (error) {
      setMensaje('Error al eliminar el pedido')
    }
  }

  return (
    <div className="contenedor">
      <header>
        <h1>Sistema de Gestión de Pedidos</h1>
        <p>Arquitectura distribuida con tolerancia a fallos</p>
      </header>

      <main>
        <section className="formulario">
          <h2>Registrar nuevo pedido</h2>

          <form onSubmit={agregarPedido}>
            <input
              type="text"
              placeholder="Nombre del cliente"
              value={cliente}
              onChange={(e) => setCliente(e.target.value)}
              required
            />

            <input
              type="text"
              placeholder="Descripción del pedido"
              value={descripcion}
              onChange={(e) => setDescripcion(e.target.value)}
              required
            />

            <button type="submit">Registrar pedido</button>
          </form>

          {mensaje && <p className="mensaje">{mensaje}</p>}
        </section>

        <section className="tabla">
          <h2>Pedidos registrados</h2>

          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Cliente</th>
                <th>Descripción</th>
                <th>Estado</th>
                <th>Acciones</th>
              </tr>
            </thead>

            <tbody>
              {pedidos.map((pedido) => (
                <tr key={pedido.id}>
                  <td>{pedido.id}</td>
                  <td>{pedido.cliente}</td>
                  <td>{pedido.descripcion}</td>
                  <td>{pedido.estado}</td>
                  <td>
                    <button onClick={() => cambiarEstado(pedido)}>
                      Cambiar estado
                    </button>

                    <button
                      className="eliminar"
                      onClick={() => eliminarPedido(pedido.id)}
                    >
                      Eliminar
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      </main>
    </div>
  )
}

export default App
