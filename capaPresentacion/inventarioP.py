from capaLogica.inventarioL import LInventario
import streamlit as st

class PInventario:
    def __init__(self):
        self.lInventario = LInventario()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("Movimientos de Inventario")

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

        self.mostrarMovimientos()

        st.subheader("Eliminar movimiento")
        id_mov = st.number_input("ID del movimiento a eliminar", min_value=1, step=1)

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
