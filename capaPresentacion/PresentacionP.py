from capaLogica.productosL import LProductos
import streamlit as st

class PProductos:
    def __init__(self):
        self.lProductos = LProductos()
        self.construirInterfaz()
#En esta parte se va a crear lo que el usuario va a mirar al final
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
                st.success("El producto se elimino")
                
                st.rerun()  
        st.divider()
        self.vistaActualizarProducto()         
#Aca va a mostrar el producto 
    def mostrarProductos(self):
        productos = self.lProductos.mostrarProductos()

        if productos and len(productos) > 0:
            st.dataframe(productos)
        else:
            st.info("No hay productos registrados")
#Con esto se ingresara nuevos productos 
    def insertarProducto(self, producto: dict):
        self.lProductos.insertarProducto(producto)
        st.toast("Producto guardado correctamente", icon="😍")
        st.rerun()
 #y con esto es para que se mire la nueva actualizacion    
    def vistaActualizarProducto(self):
        st.subheader("Actualizar Producto")

        id_producto = st.number_input(
            "ID del producto", min_value=1, step=1
        )

        nombre = st.text_input("Nuevo nombre")
        precio = st.number_input("Nuevo precio", min_value=0.0, step=0.1)
        stock = st.number_input("Nueva Cantidad", min_value=0, step=1)
        categoria = st.text_input("Nueva categoría")
        unidad = st.text_input("Nueva unidad (kg, unid, lt)")
        estado = st.selectbox("Nuevo estado", [1, 0])

        if st.button("Actualizar producto"):
            resultado = self.lProductos.actualizarProducto(
                id_producto,
                nombre,
                precio,
                stock,
                categoria,
                unidad,
                estado
            )

            if isinstance(resultado, dict) and "error" in resultado:
                st.error(resultado["error"])
            else:
                st.success("Producto actualizado correctamente")
                st.rerun()
