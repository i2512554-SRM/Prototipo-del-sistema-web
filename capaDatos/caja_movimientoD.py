"""from conexion import ConexionSupabase

class DCajaMovimientos:
    def __init__(self):
        self.__db = ConexionSupabase().conectar()
        self.__nombretabla = 'caja_movimientos'

    def __ejecutarConsulta(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                return consulta.execute().data
            else:
                return consulta.execute()
        except Exception as e:
            return f'ERROR: {e}'


    def insertarMovimiento(self, movimiento: dict):
        consulta = self.__db.table(self.__nombretabla).insert(movimiento)
        return self.__ejecutarConsulta(consulta)


    def mostrarMovimientos(self):
        consulta = self.__db.table(self.__nombretabla).select('*')
        return self.__ejecutarConsulta(consulta, 'SELECT')


    def obtenerMovimientoPorId(self, id_movimiento: int):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .select('*')
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta, 'SELECT')


    def actualizarMovimiento(self, id_movimiento: int, datos: dict):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .update(datos)
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)


    def eliminarMovimiento(self, id_movimiento: int):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .delete()
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)"""
#-----------------------------------
#Actualizacion
#---------------------------------
from conexion import ConexionSupabase

class DCajaMovimientos:
    def __init__(self):
        self.__db = ConexionSupabase().conectar()
        self.__nombretabla = 'caja_movimientos'

    def __ejecutarConsulta(self, consulta, select=False):
        try:
            resultado = consulta.execute()

            if select:
                return resultado.data

            return {"ok": True, "data": resultado.data}

        except Exception as e:
            return {"error": True, "mensaje": str(e)}

    def insertarMovimiento(self, movimiento: dict):
        consulta = self.__db.table(self.__nombretabla).insert(movimiento)
        return self.__ejecutarConsulta(consulta)

    def mostrarMovimientos(self):
        consulta = self.__db.table(self.__nombretabla).select('*')
        return self.__ejecutarConsulta(consulta, select=True)

    def obtenerMovimientoPorId(self, id_movimiento: int):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .select('*')
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta, select=True)

    def actualizarMovimiento(self, id_movimiento: int, datos: dict):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .update(datos)
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)

    def eliminarMovimiento(self, id_movimiento: int):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .delete()
            .eq('id_movimiento', id_movimiento)
        )
        return self.__ejecutarConsulta(consulta)

