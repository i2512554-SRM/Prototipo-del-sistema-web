from capaLogica.inventarioL import LInventario
import streamlit as st

class PInventario:
    def __init__(self):
        self.lInventario = LInventario()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("Movimientos de Inventario")

        movimientos = self.lInventario.mostrarMovimientosInventario()

        if movimientos:
            st.subheader("Inventario")
            st.dataframe(movimientos)

            ids = [m["id_movimiento"] for m in movimientos]
            id_seleccionado = st.selectbox("Seleccionar ID movimiento", ids)
            movimiento_sel = next(m for m in movimientos if m["id_movimiento"] == id_seleccionado)
        else:
            movimiento_sel = None

        with st.form("form_inventario"):
            id_producto = st.number_input("ID Producto", min_value=1, value=1)
            tipo = st.selectbox("Tipo", ["entrada", "salida"])
            cantidad = st.number_input("Cantidad", min_value=1, value=1)
            costo = st.number_input("Costo unitario", min_value=0.0, value=0.0)
            descripcion = st.text_area("Descripción")
            id_usuario = st.number_input("ID Usuario", min_value=1, value=1)

            btnGuardar = st.form_submit_button("Registrar")

            if btnGuardar:
                movimiento = {
                    "id_producto": id_producto,
                    "tipo": tipo,
                    "cantidad": cantidad,
                    "costo_unitario": costo,
                    "descripcion": descripcion,
                    "id_usuario": id_usuario
                }
                self.lInventario.insertarMovimientoInventario(movimiento)
                st.success("Movimiento registrado correctamente")

            if btnActualizar and movimiento_sel:
                self.lInventario.actualizarMovimientoInventario(movimiento_sel["id_movimiento"], movimiento)
                st.toast("Movimiento actualizado")

            if btnEliminar and movimiento_sel:
                self.lInventario.eliminarMovimientoInventario(movimiento_sel["id_movimiento"])
                st.toast("Movimiento eliminado")
            if st.button("Eliminar"):
                resultado = self.lInventario.eliminarMovimientoInventario(id_mov)
                if isinstance(resultado, str) and "ERROR" in resultado:
                    st.error(resultado)
                else:
                    st.success("Movimiento eliminado correctamente")
                    st.experimental_rerun() 

    def mostrarMovimientos(self):
        movimientos = self.lInventario.mostrarMovimientosInventario()
        if movimientos:
            st.subheader("Lista de Movimientos")
            st.dataframe(movimientos)
        else:
            st.info("No hay movimientos registrados")
