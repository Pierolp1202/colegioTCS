from conexion.conexion import Conexion
from flask_login import UserMixin


class Usuario(UserMixin):
    def __init__(self, nombre, rol):
        self.__nombre=nombre
        self.__rol=rol

    @property
    def rol(cls):
        return cls.__rol

    def get_id(cls):
        return cls.__nombre

    def check_password(cls, password):
        try:
            sql="SELECT usu_clave FROM usuarios WHERE usu_nombre='"+cls.__nombre+"'"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            return resultado[0]==password
        except Exception as e:
            pass
        finally:
            conexion.close()

    @classmethod
    def cargar_usuario(cls, user_id):
        try:
            sql="SELECT usu_nombre, usu_rol FROM usuarios WHERE usu_nombre='"+user_id+"'"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            if resultado is not None:
                return Usuario(resultado[0], resultado[1])
            else:
                return None

        except Exception as e:
            print(e)
        finally:
            conexion.close()