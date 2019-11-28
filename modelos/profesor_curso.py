from conexion.conexion import Conexion

class ProfesorCurso:
    def __init__(self, profesor, curso, dni, codigo):
        self.__profesor=profesor
        self.__curso=curso
        self.__dni=dni
        self.__codigo=codigo

    @property
    def profesor(cls):
        return cls.__profesor

    @property
    def curso(cls):
        return cls.__curso

    @property
    def dni(cls):
        return cls.__dni

    @property
    def codigo(cls):
        return cls.__codigo

    @classmethod
    def registrar_profesores_cursos(cls, profesor, curso):
        try:
            sql="INSERT INTO profesores_cursos(pro_cur_profesor, pro_cur_curso) VALUES('"+profesor+"', "+curso+")"
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            conexion.commit()
        except Exception as e:
            print(e)
        finally:
            conexion.close()

            
    @classmethod
    def eliminar_profesores_cursos(cls, profesor, curso):
        sql="DELETE FROM profesores_cursos WHERE pro_cur_profesor='"+profesor+"' AND pro_cur_curso="+curso
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
    def mostrar_profesores_cursos(cls):
        sql='SELECT pro_nombres, pro_ap_paterno, pro_ap_materno, cur_nombre, pro_dni, cur_codigo FROM profesores INNER JOIN profesores_cursos ON profesores.pro_dni=profesores_cursos.pro_cur_profesor INNER JOIN cursos ON cursos.cur_codigo=profesores_cursos.pro_cur_curso'
        profesores_cursos=[]
        try:
            conexion=Conexion().getConexion()
            cursor=conexion.cursor()
            cursor.execute(sql)
            result=cursor.fetchone()
            while result!=None:
                profesores_cursos.append(ProfesorCurso(result[0]+' '+result[1]+' '+result[2], result[3], result[4], result[5]))
                result=cursor.fetchone()
            return profesores_cursos
        except Exception as e:
            print(e)
        finally:
            conexion.close()
