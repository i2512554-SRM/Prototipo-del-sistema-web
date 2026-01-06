"""""
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
"""""
# capaPresentacion/inventarioP.py
"""""
from capaLogica.inventarioL import LInventario
from capaLogica.productosL import LProductos
import streamlit as st

class PInventario:
    def __init__(self):
        self.lInventario = LInventario()
        self.lProductos = LProductos()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("Movimientos de Inventario")

        # =======================
        # Selección de productos
        # =======================
        productos = self.lProductos.listarProductos()
        if productos:
            # opciones del selectbox en formato "id - nombre"
            opciones_productos = [f"{p['id_producto']} - {p['nombre']}" for p in productos]
            producto_seleccionado = st.selectbox("Seleccionar Producto", opciones_productos)
            id_producto = int(producto_seleccionado.split(" - ")[0])
        else:
            st.warning("No hay productos registrados")
            return  # No continuar si no hay productos

        # =======================
        # Mostrar movimientos
        # =======================
        movimientos = self.lInventario.mostrarMovimientosInventario()
        if movimientos:
            st.subheader("Inventario")
            st.dataframe(movimientos)
            ids = [m["id_mov"] for m in movimientos]
            id_seleccionado = st.selectbox("Seleccionar ID movimiento", ids)
            movimiento_sel = next((m for m in movimientos if m["id_mov"] == id_seleccionado), None)
        else:
            movimiento_sel = None

        # =======================
        # Formulario
        # =======================
        with st.form("form_inventario"):
            tipo = st.selectbox("Tipo", ["entrada", "salida"])
            cantidad = st.number_input("Cantidad", min_value=1, value=1)
            costo = st.number_input("Costo unitario", min_value=0.0, value=0.0)
            descripcion = st.text_area("Descripción")
            id_usuario = st.number_input("ID Usuario", min_value=1, value=1)

            btnGuardar = st.form_submit_button("Registrar")
            btnActualizar = st.form_submit_button("Actualizar")
            btnEliminar = st.form_submit_button("Eliminar")

            movimiento = {
                "id_producto": id_producto,
                "tipo": tipo,
                "cantidad": cantidad,
                "costo_unitario": costo,
                "descripcion": descripcion,
                "id_usuario": id_usuario
            }

            # =======================
            # Guardar movimiento
            # =======================
            if btnGuardar:
                resultado = self.lInventario.insertarMovimientoInventario(movimiento)
                if isinstance(resultado, str) and "ERROR" in resultado:
                    st.error(resultado)
                else:
                    st.success("Movimiento registrado correctamente")
                    st.experimental_rerun()

            # =======================
            # Actualizar movimiento
            # =======================
            if btnActualizar and movimiento_sel:
                self.lInventario.actualizarMovimientoInventario(movimiento_sel["id_mov"], movimiento)
                st.success("Movimiento actualizado")
                st.experimental_rerun()

            # =======================
            # Eliminar movimiento
            # =======================
            if btnEliminar and movimiento_sel:
                self.lInventario.eliminarMovimientoInventario(movimiento_sel["id_mov"])
                st.success("Movimiento eliminado")
                st.experimental_rerun()

"""""
from capaLogica.inventarioL import LInventario
from capaLogica.productosL import LProductos
import streamlit as st


class PInventario:
    def __init__(self):
        self.lInventario = LInventario()
        self.lProductos = LProductos()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("Movimientos de Inventario")

        # =======================
        # Session state
        # =======================
        if "accion_inventario" not in st.session_state:
            st.session_state.accion_inventario = None

        # =======================
        # Selección de productos
        # =======================
        productos = self.lProductos.listarProductos()
        if not productos:
            st.warning("No hay productos registrados")
            return

        opciones_productos = [
            f"{p['id_producto']} - {p['nombre']}" for p in productos
        ]
        producto_seleccionado = st.selectbox(
            "Seleccionar Producto", opciones_productos
        )
        id_producto = int(producto_seleccionado.split(" - ")[0])

        # =======================
        # Mostrar movimientos
        # =======================
        movimientos = self.lInventario.mostrarMovimientosInventario()
        movimiento_sel = None

        if movimientos:
            st.subheader("Inventario")
            st.dataframe(movimientos, use_container_width=True)

            ids = [m["id_mov"] for m in movimientos]
            id_seleccionado = st.selectbox(
                "Seleccionar ID movimiento", ids
            )
            movimiento_sel = next(
                (m for m in movimientos if m["id_mov"] == id_seleccionado),
                None
            )

        # =======================
        # Formulario
        # =======================
        with st.form("form_inventario", clear_on_submit=True):
            tipo = st.selectbox("Tipo", ["entrada", "salida"])
            cantidad = st.number_input("Cantidad", min_value=1, value=1)
            costo = st.number_input(
                "Costo unitario", min_value=0.0, value=0.0
            )
            descripcion = st.text_area("Descripción")
            id_usuario = st.number_input(
                "ID Usuario", min_value=1, value=1
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

            # ===== acciones =====
            if btnGuardar:
                resultado = self.lInventario.insertarMovimientoInventario(movimiento)
                if isinstance(resultado, str) and "ERROR" in resultado:
                    st.error(resultado)
                else:
                    st.session_state.accion_inventario = "guardar"

            if btnActualizar:
                if movimiento_sel:
                    self.lInventario.actualizarMovimientoInventario(
                        movimiento_sel["id_mov"], movimiento
                    )
                    st.session_state.accion_inventario = "actualizar"
                else:
                    st.warning("Seleccione un movimiento para actualizar")

            if btnEliminar:
                if movimiento_sel:
                    self.lInventario.eliminarMovimientoInventario(
                        movimiento_sel["id_mov"]
                    )
                    st.session_state.accion_inventario = "eliminar"
                else:
                    st.warning("Seleccione un movimiento para eliminar")

        # =======================
        # Mensajes + rerun (FUERA del form)
        # =======================
        if st.session_state.accion_inventario:
            if st.session_state.accion_inventario == "guardar":
                st.success("Movimiento registrado correctamente")
            elif st.session_state.accion_inventario == "actualizar":
                st.success("Movimiento actualizado correctamente")
            elif st.session_state.accion_inventario == "eliminar":
                st.success("Movimiento eliminado correctamente")

            st.session_state.accion_inventario = None
            st.rerun()
