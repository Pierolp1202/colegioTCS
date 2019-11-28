from conexion.conexion import Conexion


class Etapa:
    def __init__(self, numero, nombre):
        self.__numero=numero
        self.__nombre=nombre

    
    @property
    def numero(cls):
        return cls.__numero

    @numero.setter
    def numero(cls, codigo):
        cls.__numero=numero

    @property
    def nombre(cls):
        return cls.__nombre

    @nombre.setter
    def nombre(cls, nombre):
        cls.__nombre=nombre

    @classmethod
    def registrar_etapa(cls, nombre):
        sql="INSERT INTO etapas(eta_nombre) VALUES('"+nombre+"')"
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
    def cargar_etapas(cls):
        etapas=[]
        sql='SELECT eta_nombre, eta_numero FROM  etapas'
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            while resultado!=None:
                etapas.append(Etapa(resultado[1], resultado[0]))
                resultado=cursor.fetchone()
                print(resultado)
            return etapas
        except Exception as e:
            print(e)
        finally:
            conexion.close()


    @classmethod
    def eliminar_etapa(cls, nombre):
        sql="DELETE FROM  etapas WHERE eta_nombre='"+nombre+"'"
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()