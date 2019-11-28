from conexion.conexion import Conexion

class Nivel:
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
    def registrar_nivel(cls, nombre):
        try:
            sql="INSERT INTO niveles(niv_nombre) VALUES('"+nombre+"')"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()

    @classmethod
    def cargar_niveles(cls):
        niveles=[]
        sql='SELECT niv_nombre, niv_numero FROM  niveles'
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            while resultado!=None:
                niveles.append(Nivel(resultado[0], resultado[1]))
                resultado=cursor.fetchone()
            return niveles
        except Exception as e:
            print(e)
        finally:
            conexion.close()


    @classmethod
    def eliminar_nivel(cls, nombre):
        sql="DELETE FROM  niveles WHERE niv_nombre='"+nombre+"'"
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()