from capaDatos.productoD import DProductos

class LProductos:
    def __init__(self):
        self.dProductos = DProductos()

    def mostrarProductos(self):
        return self.dProductos.mostrarProductos()

    def insertarProducto(self, producto: dict):
        # Validaciones básicas
        if producto["precio"] <= 0:
            return "ERROR: El precio debe ser mayor a 0"
        if producto["stock"] < 0:
            return "ERROR: El stock no puede ser negativo"

        return self.dProductos.insertarProducto(producto)
    def eliminarProducto(self, id_producto: int):
        if id_producto <= 0:
            return "ERROR: ID de producto inválido"

        return self.dProductos.eliminarProducto(id_producto)
