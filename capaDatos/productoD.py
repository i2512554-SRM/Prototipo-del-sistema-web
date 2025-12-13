from conexion import ConexionSupabase

class DProductos:
    def __init__(self):
        self.__db = ConexionSupabase().conectar()
        self.__nombretabla = 'productos'

    def __ejecutarConsulta(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                return consulta.execute().data
            else:
                return consulta.execute()
        except Exception as e:
            return f'ERROR: {e}'

    def mostrarProductos(self):
        consulta = self.__db.table(self.__nombretabla).select('*')
        return self.__ejecutarConsulta(consulta, 'SELECT')

    def insertarProducto(self, producto: dict):
        consulta = self.__db.table(self.__nombretabla).insert(producto)
        return self.__ejecutarConsulta(consulta)


    def eliminarProducto(self, id_producto: int):
        consulta = self.__db.table(self.__nombretabla) \
            .delete() \
            .eq('id_producto', id_producto)

        return self.__ejecutarConsulta(consulta)
