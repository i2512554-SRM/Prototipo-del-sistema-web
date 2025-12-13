from conexion import ConexionSupabase

class DInventario:
    def __init__(self):
        self.__db = ConexionSupabase().conectar()
        self.__nombretabla = 'inventario_movimientos'

    def __ejecutarConsulta(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                return consulta.execute().data
            else:
                return consulta.execute()
        except Exception as e:
            return f'ERROR: {e}'

    def mostrarMovimientosInventario(self):
        consulta = self.__db.table(self.__nombretabla).select('*')
        return self.__ejecutarConsulta(consulta, 'SELECT')

    def insertarMovimientoInventario(self, movimiento: dict):
        consulta = self.__db.table(self.__nombretabla).insert(movimiento)
        return self.__ejecutarConsulta(consulta)
