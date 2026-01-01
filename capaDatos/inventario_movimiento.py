"""""
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

    def actualizarMovimientoInventario(self, id_mov: int, datos: dict):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .update(datos)
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)

    def eliminarMovimientoInventario(self, id_mov: int):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .delete()
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)
"""""
from conexion import ConexionSupabase

class DInventario:
    def __init__(self):
        self.__db = ConexionSupabase().conectar()
        self.__tabla_mov = 'inventario_movimientos'
        self.__tabla_prod = 'productos'

    def __ejecutarConsulta(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                return consulta.execute().data
            else:
                return consulta.execute()
        except Exception as e:
            return f'ERROR: {e}'


    def mostrarMovimientosInventario(self):
        consulta = self.__db.table(self.__tabla_mov).select('*')
        return self.__ejecutarConsulta(consulta, 'SELECT')

    def insertarMovimientoInventario(self, movimiento: dict):
        consulta = self.__db.table(self.__tabla_mov).insert(movimiento)
        return self.__ejecutarConsulta(consulta)

    def actualizarMovimientoInventario(self, id_mov: int, datos: dict):
        consulta = (
            self.__db
            .table(self.__tabla_mov)
            .update(datos)
            .eq('id_mov', id_mov)
        )
        return self.__ejecutarConsulta(consulta)

    def eliminarMovimientoInventario(self, id_mov: int):
        consulta = (
            self.__db
            .table(self.__tabla_mov)
            .delete()
            .eq('id_mov', id_mov)
        )
        return self.__ejecutarConsulta(consulta)


    def listarProductos(self):
        consulta = self.__db.table(self.__tabla_prod).select('id_mov', 'nombre')
        return self.__ejecutarConsulta(consulta, 'SELECT')
