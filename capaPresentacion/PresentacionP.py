from capaLogica.productosL import LProductos
import streamlit as st

class PProductos:
    def __init__(self):
        self.lProductos = LProductos()
        self.construirInterfaz()

    def construirInterfaz(self):
        st.title("Gestión de Productos")

        with st.form("form_producto"):
            nombre = st.text_input("Nombre del producto")
            precio = st.number_input("Precio", min_value=0.0)
            stock = st.number_input("Stock", min_value=0)
            categoria = st.text_input("Categoría")
            unidad = st.text_input("Unidad (kg, unid, lt)")
            estado = st.selectbox("Estado", [1, 0])

            btnGuardar = st.form_submit_button("Guardar", type="primary")

            if btnGuardar:
                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "stock": stock,
                    "categoria": categoria,
                    "unidad": unidad,
                    "estado": estado
                }
                self.insertarProducto(producto)

        
        self.mostrarProductos()

    
        st.subheader("Eliminar producto")

        id_producto = st.number_input(
            "ID del producto a eliminar",
            min_value=1,
            step=1
        )

        if st.button("Eliminar", type="primary"):
            resultado = self.lProductos.eliminarProducto(id_producto)

            if isinstance(resultado, str) and "ERROR" in resultado:
                st.error(resultado)
            else:
                st.success("Producto eliminado correctamente")
                st.rerun()  

    def mostrarProductos(self):
        productos = self.lProductos.mostrarProductos()

        if productos and len(productos) > 0:
            st.dataframe(productos)
        else:
            st.info("No hay productos registrados")

    def insertarProducto(self, producto: dict):
        self.lProductos.insertarProducto(producto)
        st.toast("Producto guardado correctamente", icon="😍")