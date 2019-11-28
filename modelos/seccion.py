from conexion.conexion import Conexion

class Seccion:
    def __init__(self, nombre, numero):
        self.__nombre=nombre
        self.__numero=numero

    
    @property
    def nombre(cls):
        return cls.__nombre

    @nombre.setter
    def nombre(cls, nombre):
        cls.__nombre=nombre

    @property
    def numero(cls):
        return cls.__numero

    @numero.setter
    def numero(cls, numero):
        cls.__numero=numero


    @classmethod
    def registrar_seccion(cls, nombre):
        try:
            sql="INSERT INTO secciones(sec_nombre) VALUES('"+nombre+"')"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()

    @classmethod
    def cargar_secciones(cls):
        etapas=[]
        sql='SELECT sec_nombre, sec_numero FROM  secciones'
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            while resultado!=None:
                etapas.append(Seccion(resultado[0], resultado[1]))
                resultado=cursor.fetchone()
                print(resultado)
            return etapas
        except Exception as e:
            print(e)
        finally:
            conexion.close()


    @classmethod
    def eliminar_seccion(cls, nombre):
        sql="DELETE FROM  secciones WHERE sec_nombre='"+nombre+"'"
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()