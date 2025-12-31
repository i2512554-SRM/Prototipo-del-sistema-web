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

    def actualizarMovimientoInventario(self, id_movimiento: int, datos: dict):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .update(datos)
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)

    def eliminarMovimientoInventario(self, id_movimiento: int):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .delete()
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)
