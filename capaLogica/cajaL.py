"""from capaDatos.caja_movimientoD import DCajaMovimientos

class LCaja:
    def __init__(self):
        self.dCaja = DCajaMovimientos()

    def mostrarMovimientos(self):
        return self.dCaja.mostrarMovimientos()

    def insertarMovimiento(self, movimiento: dict):
        if movimiento["monto"] <= 0:
            return "ERROR: El monto debe ser mayor a 0"

        if movimiento["tipo"] not in ["ingreso", "egreso"]:
            return "ERROR: Tipo de movimiento inválido"

        return self.dCaja.insertarMovimiento(movimiento)"""
#-----------------------------------
#Actualizacion
#---------------------------------
from capaDatos.caja_movimientoD import DCajaMovimientos

class LCaja:
    def __init__(self):
        self.dCaja = DCajaMovimientos()

    def mostrarMovimientos(self):
        return self.dCaja.mostrarMovimientos()

    def insertarMovimiento(self, movimiento: dict):

        if "monto" not in movimiento or "tipo" not in movimiento:
            return {"error": True, "mensaje": "Datos incompletos"}

        if movimiento["monto"] <= 0:
            return {"error": True, "mensaje": "El monto debe ser mayor a 0"}

        if movimiento["tipo"] not in ["ingreso", "egreso"]:
            return {"error": True, "mensaje": "Tipo inválido"}

        return self.dCaja.insertarMovimiento(movimiento)


    def actualizarMovimiento(self, id_movimiento: int, datos: dict):

        if "monto" in datos and datos["monto"] <= 0:
            return {"error": True, "mensaje": "El monto debe ser mayor a 0"}

        if "tipo" in datos and datos["tipo"] not in ["ingreso", "egreso"]:
            return {"error": True, "mensaje": "Tipo inválido"}

        return self.dCaja.actualizarMovimiento(id_movimiento, datos)


    def eliminarMovimiento(self, id_movimiento: int):
        return self.dCaja.eliminarMovimiento(id_movimiento)

