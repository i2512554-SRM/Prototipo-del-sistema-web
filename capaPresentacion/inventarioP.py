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
            id_producto = st.number_input(
                "ID Producto", value=movimiento_sel["id_producto"] if movimiento_sel else 1
            )
            tipo = st.selectbox(
                "Tipo", ["entrada", "salida"],
                index=0 if not movimiento_sel else ["entrada", "salida"].index(movimiento_sel["tipo"])
            )
            cantidad = st.number_input(
                "Cantidad", min_value=1,
                value=movimiento_sel["cantidad"] if movimiento_sel else 1
            )
            costo = st.number_input(
                "Costo unitario", min_value=0.0,
                value=movimiento_sel["costo_unitario"] if movimiento_sel else 0.0
            )
            descripcion = st.text_area(
                "Descripción", value=movimiento_sel["descripcion"] if movimiento_sel else ""
            )
            id_usuario = st.number_input(
                "ID Usuario", value=movimiento_sel["id_usuario"] if movimiento_sel else 1
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                btnGuardar = st.form_submit_button("Registrar")
            with col2:
                btnActualizar = st.form_submit_button("Actualizar")
            with col3:
                btnEliminar = st.form_submit_button("Eliminar")

            movimiento = {
                "id_producto": id_producto,
                "tipo": tipo,
                "cantidad": cantidad,
                "costo_unitario": costo,
                "descripcion": descripcion,
                "id_usuario": id_usuario
            }

            if btnGuardar:
                self.lInventario.insertarMovimientoInventario(movimiento)
                st.toast("Movimiento registrado")

            if btnActualizar and movimiento_sel:
                self.lInventario.actualizarMovimientoInventario(movimiento_sel["id_movimiento"], movimiento)
                st.toast("Movimiento actualizado")

            if btnEliminar and movimiento_sel:
                self.lInventario.eliminarMovimientoInventario(movimiento_sel["id_movimiento"])
                st.toast("Movimiento eliminado")

