from capaLogica.cajaL import LCaja
import streamlit as st
import re
class PCaja:
    def __init__(self):
        self.LCaja = LCaja()
        self.construirInterfaz()
    def _solo_texto(self, texto: str) -> bool:
        return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", texto))
    def construirInterfaz(self):

        st.title("Movimientos de Caja")

        with st.form("form_caja"):
            tipo = st.selectbox("Tipo", ["ingreso", "egreso"])
            monto = st.number_input("Monto", min_value=0.0)
            categoria = st.text_input("Categoría(Tener en cuenta tiene que tener relacion con la empresa)")
            descripcion = st.text_area("Descripción")
            id_usuario = st.number_input("ID UsuarioU(Utilizar un ID del 5 al 8 )", min_value=1)
            

            btnGuardar = st.form_submit_button("Registrar", type="primary")

        if btnGuardar:

            if not categoria.strip():
                st.error("La categoría no puede estar vacía")
                return

            if not self._solo_texto(categoria):
                st.error("La categoría solo debe contener letras")
                return

            movimiento = {
                    "tipo": tipo,
                    "monto": monto,
                    "categoria": categoria,
                    "descripcion": descripcion,
                    "id_usuario": id_usuario,
                }

            resultado = self.insertarMovimiento(movimiento)

            if resultado and isinstance(resultado, dict) and "error" in resultado:
                st.error(resultado.get("mensaje", "Error al registrar"))
            else:
                st.toast("Movimiento registrado", icon="😁")
                st.rerun()

                resultado = self.insertarMovimiento(movimiento)

                if resultado and isinstance(resultado, dict) and "error" in resultado:
                    st.error(resultado["mensaje"])
                else:
                    st.toast("Movimiento registrado", icon="💵")
                    st.rerun()

        self.mostrarMovimientos()

        st.subheader("Actualizar / Eliminar movimiento")

        id_movimiento = st.number_input("ID del movimiento", min_value=1, step=1)

        tipo_u = st.selectbox("Tipo (actualizar)", ["ingreso", "egreso"])
        monto_u = st.number_input("Monto (actualizar)", min_value=0.0)
        categoria_u = st.text_input("Categoría (actualizar)(Tener en cuenta tiene que tener relacion con la empresa)")
        descripcion_u = st.text_area("Descripción (actualizar)")
        id_usuario_u = st.number_input("ID Usuario (actualizar)(Utilizar un ID del 5 al 8)", min_value=1)
        
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
                st.success("Movimiento actualizado")
                st.rerun()

        with col2:
            if st.button("Eliminar"):
                self.LCaja.eliminarMovimiento(id_movimiento)
                st.warning("Movimiento eliminado")
                st.rerun()

    def mostrarMovimientos(self):
        movimientos = self.LCaja.mostrarMovimientos()

        if isinstance(movimientos, list) and len(movimientos) > 0:
            st.dataframe(movimientos)
        else:
            st.info("No hay movimientos registrados.")

    def insertarMovimiento(self, movimiento: dict):
        return self.LCaja.insertarMovimiento(movimiento)
