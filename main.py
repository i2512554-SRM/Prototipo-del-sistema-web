import streamlit as st
from capaPresentacion.PresentacionP import PProductos
from capaPresentacion.cajaP import PCaja
from capaPresentacion.inventarioP import PInventario

def main():
    st.set_page_config(
        page_title="Bendito Buffet",
        layout="wide"
    )

    st.sidebar.title("Bendito Buffet")

    opcion = st.sidebar.selectbox(
        "Menú",
        ["Productos", "Caja", "Inventario"]
    )

    if opcion == "Productos":
        PProductos()
    elif opcion == "Caja":
        PCaja()
    elif opcion == "Inventario":
        PInventario()

if __name__ == "__main__":
    main()
