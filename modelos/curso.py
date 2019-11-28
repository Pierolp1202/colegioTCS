from conexion.conexion import Conexion


class Curso:
    def __init__(self, codigo, nombre):
        self.__codigo=codigo
        self.__nombre=nombre

    @property
    def codigo(cls):
        return cls.__codigo

    @property
    def nombre(cls):
        return cls.__nombre

    @classmethod
    def registrar_curso(cls, nombre):
        sql="INSERT INTO cursos(cur_nombre) VALUES('"+nombre+"')"
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
    def eliminar_curso(cls, codigo):
        sql="DELETE FROM cursos WHERE cur_codigo="+str(codigo)
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
    def cargar_cursos(cls):
        cursos=[]
        sql='SELECT cur_codigo, cur_nombre FROM cursos'
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            result=cursor.fetchone()
            while result!=None:
                cursos.append(Curso(result[0], result[1]))
                result=cursor.fetchone()
            return cursos
        except Exception as e:
            print(e)
        finally:
            conexion.close()
