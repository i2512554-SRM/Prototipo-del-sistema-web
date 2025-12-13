from capaDatos.inventario_movimiento import DInventario

class LInventario:
    def __init__(self):
        self.dInventario = DInventario()

    def mostrarMovimientosInventario(self):
        return self.dInventario.mostrarMovimientosInventario()

    def insertarMovimientoInventario(self, movimiento: dict):
        if movimiento["cantidad"] <= 0:
            return "ERROR: La cantidad debe ser mayor a 0"

        if movimiento["tipo"] not in ["entrada", "salida"]:
            return "ERROR: Tipo de movimiento inválido"

        return self.dInventario.insertarMovimientoInventario(movimiento)
