import pymysql.cursors
from conexion.singleton import MetaSingleton



class Conexion(metaclass=MetaSingleton):
    def __init__(self):
        self.__host='localhost'
        self.__port=3306
        self.__db='colegio'
        self.__user='root'
        self.__password='mysql'


    def getConexion(cls):
        return pymysql.connect(host=cls.__host, port=cls.__port, db=cls.__db, user=cls.__user, password=cls.__password)
