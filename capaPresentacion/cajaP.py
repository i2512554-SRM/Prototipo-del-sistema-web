from capaLogica.cajaL import LCaja
import streamlit as st
class PCaja:
    def __init__(self):
        self.LCaja = LCaja()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("Movimientos de Caja")

       
        with st.form("form_caja"):
            tipo = st.selectbox("Tipo", ["ingreso", "egreso"])
            monto = st.number_input("Monto", min_value=0.0)
            categoria = st.text_input("Categoría")
            descripcion = st.text_area("Descripción")
            id_usuario = st.number_input("ID Usuario", min_value=1)

            btnGuardar = st.form_submit_button("Registrar", type="primary")

            if btnGuardar:
                movimiento = {
                    "tipo": tipo,
                    "monto": monto,
                    "categoria": categoria,
                    "descripcion": descripcion,
                    "id_usuario": id_usuario
                }
                self.insertarMovimiento(movimiento)

        self.mostrarMovimientos()

       
        st.subheader(" Actualizar /  Eliminar movimiento")

        id_movimiento = st.number_input(
            "ID del movimiento",
            min_value=1,
            step=1
        )

        tipo_u = st.selectbox("Tipo (actualizar)", ["ingreso", "egreso"])
        monto_u = st.number_input("Monto (actualizar)", min_value=0.0)
        categoria_u = st.text_input("Categoría (actualizar)")
        descripcion_u = st.text_area("Descripción (actualizar)")
        id_usuario_u = st.number_input("ID Usuario (actualizar)", min_value=1)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Actualizar"):
                datos_actualizados = {
                    "tipo": tipo_u,
                    "monto": monto_u,
                    "categoria": categoria_u,
                    "descripcion": descripcion_u,
                    "id_usuario": id_usuario_u
                }
                self.LCaja.actualizarMovimiento(id_movimiento, datos_actualizados)
                st.success("Movimiento actualizado correctamente")

        with col2:
            if st.button("Eliminar"):
                self.LCaja.eliminarMovimiento(id_movimiento)
                st.warning("Movimiento eliminado")

    def mostrarMovimientos(self):
        movimientos = self.LCaja.mostrarMovimientos()
        st.dataframe(movimientos)

    def insertarMovimiento(self, movimiento: dict):
        self.LCaja.insertarMovimiento(movimiento)
        st.toast("Movimiento registrado", icon="💵")