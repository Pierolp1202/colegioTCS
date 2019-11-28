from conexion.conexion import Conexion


class Grado:
    def __init__(self, codigo, etapa, seccion, nivel, aula):
        self.__codigo=codigo
        self.__etapa=etapa
        self.__seccion=seccion
        self.__nivel=nivel
        self.__aula=aula

    @property
    def codigo(cls):
        return cls.__codigo
    
    @codigo.setter
    def codigo(cls, codigo):
        cls.__codigo=codigo

    @property
    def etapa(cls):
        return cls.__etapa

    @etapa.setter
    def etapa(cls, etapa):
        cls.__etapa=etapa


    @property
    def seccion(cls):
        return cls.__seccion

    @seccion.setter
    def seccion(cls, seccion):
        cls.__seccion=seccion

    @property
    def nivel(cls):
        return cls.__nivel

    @nivel.setter
    def nivel(cls, nivel):
        cls.__nivel=nivel

    @property
    def aula(cls):
        return cls.__aula

    @aula.setter
    def aula(cls, aula):
        cls.__aula=aula

    @classmethod
    def registrar_grado(cls, etapa, seccion, nivel, aula):
        try:
            sql="INSERT INTO grados(gra_etapa, gra_seccion, gra_nivel, gra_aula) VALUES('"+etapa+"', '"+seccion+"', '"+nivel+"', '"+aula+"')"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()

    
    @classmethod
    def cargar_grados(cls):
        try:
            grados=[]
            sql="SELECT gra_codigo, eta_nombre, sec_nombre, niv_nombre, gra_aula FROM grados AS g INNER JOIN etapas AS e ON g.gra_etapa=e.eta_numero INNER JOIN secciones AS s ON g.gra_seccion=s.sec_numero INNER JOIN niveles AS n ON g.gra_nivel=n.niv_numero;"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            resultado=cursor.fetchone()
            while resultado!=None:
                grados.append(Grado(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4]))
                resultado=cursor.fetchone()
            return grados
        except Exception as e:
            print(e)
        finally:
            conexion.close()

    @classmethod
    def eliminar_grado(cls, codigo):
        try:
            sql="DELETE FROM grados WHERE gra_codigo="+codigo
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()


        