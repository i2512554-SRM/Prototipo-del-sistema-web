from conexion import ConexionSupabase

class DUsuarios:
    def __init__(self):
        self.__db = ConexionSupabase().conectar()
        self.__nombretabla = 'usuarios'

    def __ejecutarConsulta(self, consulta, tipoConsulta=None):
        try:
            if tipoConsulta == 'SELECT':
                return consulta.execute().data
            else:
                return consulta.execute()
        except Exception as e:
            return f'ERROR: {e}'


    def mostrarUsuarios(self):
        consulta = self.__db.table(self.__nombretabla).select('*')
        return self.__ejecutarConsulta(consulta, 'SELECT')


    def insertarUsuario(self, usuario: dict):
        consulta = self.__db.table(self.__nombretabla).insert(usuario)
        return self.__ejecutarConsulta(consulta)
