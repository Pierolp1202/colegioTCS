from conexion.conexion import Conexion


class Aula:
    def __init__(self, codigo, capacidad, piso):
        self.__codigo = codigo
        self.__capacidad = capacidad
        self.__piso = piso


    @property
    def codigo(cls):
        return cls.__codigo


    @codigo.setter
    def codigo(cls):
        cls.__codigo = codigo


    @property
    def capacidad(cls):
        return cls.__capacidad


    @capacidad.setter
    def capacidad(cls):
        cls.__capacidad = capacidad


    @property
    def piso(cls):
        return cls.__piso


    @piso.setter
    def piso(cls):
        cls.__piso = piso

    @classmethod
    def eliminar_aula(cls,codigo):
        sql="DELETE FROM aulas WHERE aul_codigo='"+codigo+"'"
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()

    @classmethod
    def registrar_aula(cls, codigo, capacidad, piso):
        try:
            sql = "INSERT INTO aulas(aul_codigo, aul_capacidad, aul_piso) VALUES('" + \
                codigo+"','"+capacidad+"','"+piso+"')"
            conexion = Conexion().getConexion()
            cursor = conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            pass
        finally:
            conexion.close()


    @classmethod
    def cargar_aulas(cls):
        try:
            aulas = []
            sql = 'SELECT aul_codigo, aul_capacidad, aul_piso FROM aulas'
            conexion = Conexion().getConexion()
            cursor = conexion.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchone()
            while resultado != None:
                aulas.append(Aula(resultado[0], resultado[1], resultado[2]))
                resultado = cursor.fetchone()
            return aulas
        except Exception as e:
            print(e,'***************************')
        finally:
            conexion.close()
