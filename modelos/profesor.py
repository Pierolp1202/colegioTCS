from conexion.conexion import Conexion


class Profesor:
    def __init__(self, dni, nombres, paterno, materno, celular, correo=None):
        self.__dni=dni
        self.__nombres=nombres
        self.__paterno=paterno
        self.__materno=materno
        self.__celular=celular
        self.__correo=correo

    @property
    def dni(cls):
        return cls.__dni

    @dni.setter
    def dni(cls, dni):
        cls.__dni=dni
    

    @property
    def nombres(cls):
        return cls.__nombres
    
    @nombres.setter
    def nombres(cls, nombres):
        cls.__nombres=nombres


    @property
    def paterno(cls):
        return cls.__paterno

    @paterno.setter
    def paterno(cls, paterno):
        cls.__paterno=paterno

    
    @property
    def materno(cls):
        return cls.__materno

    @materno.setter
    def materno(cls, materno):
        cls.__materno=materno

    
    @property
    def celular(cls):
        return cls.__celular

    @celular.setter
    def celular(cls, celular):
        cls.__celular=celular

    @property
    def correo(cls):
        return cls.__correo

    @correo.setter
    def correo(cls, correo):
        cls.__correo=correo


    @classmethod
    def eliminar_profesor(cls, dni):
        sql="DELETE FROM profesores WHERE pro_dni='"+dni+"'"
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
    def registrar_profesor(cls, dni, nombres, paterno, materno, celular, correo, rol):
        try:
            sql1="INSERT INTO usuarios(usu_nombre, usu_clave, usu_rol) VALUES('"+paterno[:2]+dni[:2]+"','"+paterno[:2]+dni[:2]+"','"+rol+"')"
            sql="INSERT INTO profesores(pro_dni, pro_nombres, pro_ap_paterno, pro_ap_materno, pro_celular, pro_correo) VALUES('"+dni+"','"+nombres+"','"+paterno+"','"+materno+"','"+celular+"','"+correo+"')"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            cursor.execute(sql1)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()

    @classmethod
    def cargar_profesores(cls):
        try:
            profesores=[]
            sql="SELECT pro_dni, pro_nombres, pro_ap_paterno, pro_ap_materno, pro_celular,pro_celular FROM  profesores "
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            while resultado!=None:
                profesores.append(Profesor(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],resultado[5]))
                resultado=cursor.fetchone()
            return profesores
        except Exception as e:
            print(e)
        finally:
            conexion.close()