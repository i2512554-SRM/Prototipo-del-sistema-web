from capaDatos.caja_movimientoD import DCajaMovimientos

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

        return self.dCaja.insertarMovimiento(movimiento)
