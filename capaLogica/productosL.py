import re
from capaDatos.productoD import DProductos

class LProductos:
    def __init__(self):
        print("Cargando LProductos actualizado")
        self.dProductos = DProductos()

#Esto es para que solo puedan escribir texto 
    def _solo_texto(self, texto: str) -> bool:
        if not texto:
            return False
        return bool(re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$', texto))

#esto nos sirve para mostrar el producto
    def mostrarProductos(self):
        return self.dProductos.mostrarProductos()

#Aca insertamos y validamos que efectivamente ingresen datos permitido 
    def insertarProducto(self, producto: dict):

        if not self._solo_texto(producto["nombre"]):
            return {"error": "El nombre no debe contener números ni símbolos"}

        if not self._solo_texto(producto["categoria"]):
            return {"error": "La categoría no debe contener números"}

        if producto["unidad"] not in ["kg", "unid", "lt"]:
            return {"error": "Unidad inválida"}

        if producto["precio"] <= 0:
            return {"error": "Precio inválido"}

        if producto["stock"] < 0:
            return {"error": "Stock inválido"}

        producto["estado"]

        return self.dProductos.insertarProducto(producto)

#Esto sirve para eliminar algun producto 
    def eliminarProducto(self, id_producto: int):
        if id_producto <= 0:
            return {"error": "ID inválido"}
        return self.dProductos.eliminarProducto(id_producto)

#Con esto actualizamos 
    def actualizarProducto(self, id_producto, nombre, precio, stock, categoria, unidad, estado):

        if not self._solo_texto(nombre):
            return {"error": "Nombre inválido"}

        if not self._solo_texto(categoria):
            return {"error": "Categoría inválida"}

        if precio <= 0 or stock < 0:
            return {"error": "Precio o stock inválido"}

        if unidad not in ["kg", "unid", "lt"]:
            return {"error": "Unidad inválida"}

        return self.dProductos.actualizarProducto(
            id_producto, nombre, precio, stock, categoria, unidad, estado
        )
    def listarProductos(self):
        productos = self.dProductos.mostrarProductos()
        return [dict(p) for p in productos]

"""  
    def listarProductos(self):
        productos = self.dProductos.mostrarProductos()
        return productos if productos else []
"""""
