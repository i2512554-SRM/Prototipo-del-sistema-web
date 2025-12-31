from conexion import ConexionSupabase

class DProductos:
    def __init__(self):
        self.__db = ConexionSupabase().conectar()
        self.__nombretabla = 'productos'

#En esta parte se ejecuta todo desde un inicio como inica desde arriba pa abajo uno por uno para iniciar desde el principo bien 
    def __ejecutarConsulta(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                return consulta.execute().data
            else:
                return consulta.execute()
        except Exception as e:
            return f'ERROR: {e}'
#Esta funcion como su mismo nombre dice es para mostrar los productos existentes
    def mostrarProductos(self):
        consulta = self.__db.table(self.__nombretabla).select('*')
        return self.__ejecutarConsulta(consulta, 'SELECT')
#Esta parte es para poner insertar un nuevo producto 
    def insertarProducto(self, producto: dict):
        consulta = self.__db.table(self.__nombretabla).insert(producto)
        return self.__ejecutarConsulta(consulta)
#Esta parte es para eliminar algun producto que no este en stock
    def eliminarProducto(self, id_producto: int):
        consulta = self.__db.table(self.__nombretabla) \
            .delete() \
            .eq('id_producto', id_producto)

        return self.__ejecutarConsulta(consulta)
#Esta funcion es para poder actualizar algun producto mayormente para evitar productos con id's duplicados
    def actualizarProducto(self, id_producto, nombre, precio, stock, categoria, unidad, estado):
        consulta = (
            self.__db
            .table(self.__nombretabla)
            .update({
                "nombre": nombre,
                "precio": precio,
                "stock": stock,
                "categoria": categoria,
                "unidad": unidad,
                "estado": estado
            })
            .eq("id_producto", id_producto)
        )

        return self.__ejecutarConsulta(consulta)

