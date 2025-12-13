from capaLogica.inventarioL import LInventario
import streamlit as st

class PInventario:
    def __init__(self):
        self.lInventario = LInventario()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title(" Movimientos de Inventario")

        with st.form("form_inventario"):
            id_producto = st.number_input("ID Producto", min_value=1)
            tipo = st.selectbox("Tipo", ["entrada", "salida"])
            cantidad = st.number_input("Cantidad", min_value=1)
            costo = st.number_input("Costo unitario", min_value=0.0)
            descripcion = st.text_area("Descripción")
            id_usuario = st.number_input("ID Usuario", min_value=1)

            btnGuardar = st.form_submit_button("Registrar", type="primary")

            if btnGuardar:
                movimiento = {
                    "id_producto": id_producto,
                    "tipo": tipo,
                    "cantidad": cantidad,
                    "costo_unitario": costo,
                    "descripcion": descripcion,
                    "id_usuario": id_usuario
                }
                self.insertarMovimientoInventario(movimiento)

        self.mostrarInventario()

    def mostrarInventario(self):
        movimientos = self.lInventario.mostrarMovimientosInventario()
        st.dataframe(movimientos)

    def insertarMovimientoInventario(self, movimiento: dict):
        self.lInventario.insertarMovimientoInventario(movimiento)
        st.toast("Movimiento de inventario registrado", icon="📦")
