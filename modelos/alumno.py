from conexion.conexion import Conexion

class Alumno:
    def __init__(self, dni, nombres, paterno, materno, grado, edad, sexo, apoderado):
        self.__dni=dni
        self.__nombres=nombres
        self.__paterno=paterno
        self.__materno=materno
        self.__grado=grado
        self.__edad=edad
        self.__sexo=sexo
        self.__apoderado=apoderado

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
    def grado(cls):
        return cls.__grado

    @grado.setter
    def grado(cls, grado):
        cls.__grado=grado

    
    @property
    def edad(cls):
        return cls.__edad

    @edad.setter
    def edad(cls, edad):
        cls.__edad=edad

    
    @property
    def sexo(cls):
        return cls.__sexo

    @sexo.setter
    def sexo(cls, sexo):
        cls.__sexo=sexo

    
    @property
    def apoderado(cls):
        return cls.__apoderado

    @apoderado.setter
    def apoderado(cls, apoderado):
        cls.__apoderado=apoderado



    @classmethod
    def registrar_alumnos(cls, dni, nombres, paterno, materno, grado, edad, sexo, apoderado):
        try:
            sql="INSERT INTO alumnos(alu_dni, alu_nombres, alu_paterno, alu_materno, alu_grado, alu_edad, alu_sexo, alu_apoderado) VALUES('"+dni+"', '"+nombres+"', '"+paterno+"', '"+materno+"', "+grado+", "+edad+", '"+sexo+"', '"+apoderado+"')"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()


    @classmethod
    def filtrar_alumnos(cls,codigo):
        try:
            alumnos=[]
            sql="SELECT alu_dni, alu_nombres, alu_paterno, alu_materno, alu_grado, alu_edad, alu_sexo, alu_apoderado  FROM alumnos AS a INNER JOIN grados AS g ON a.alu_grado=g.gra_codigo WHERE g.gra_codigo="+str(codigo)
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            result=cursor.fetchone()
            while result !=None:
                alumnos.append(Alumno(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7]))
                result=cursor.fetchone()
            return alumnos
        except Exception as e:
            print(e)
        finally:
            conexion.close()    

    @classmethod
    def cargar_alumnos(cls):
        try:
            alumnos=[]
            sql="SELECT alu_dni, alu_nombres, alu_paterno, alu_materno, CONCAT(eta_nombre, ' \\'' ,sec_nombre,'\\' ', niv_nombre) AS grado, alu_edad, alu_sexo, alu_apoderado FROM alumnos AS a INNER JOIN grados AS g ON a.alu_grado=g.gra_codigo INNER JOIN etapas AS e ON e.eta_numero=g.gra_etapa INNER JOIN secciones AS s ON s.sec_numero=g.gra_seccion INNER JOIN niveles AS n ON n.niv_numero=g.gra_nivel"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            while resultado!=None:
                alumnos.append(Alumno(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6], resultado[7]))
                resultado=cursor.fetchone()
            return alumnos
        except Exception as e:
            print(e)
        finally:
            conexion.close()

    @classmethod
    def eliminar_alumno(cls, dni):
        sql="DELETE FROM alumnos WHERE alu_dni='"+dni+"'"
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()
            