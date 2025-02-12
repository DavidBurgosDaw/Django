class Asignatura():
    def __init__(self,nombre,profesor,numero,hSemanales,imagen):
        self.__nombre = nombre
        self.__profesor = profesor
        self.__numero = numero
        self.__hSemanales = hSemanales
        self.__imagen = imagen #Url Imagen a mostrar

        #Metodos Get

    @property
    def nombre(self):
        return self.__nombre
    @property
    def profesor(self):
        return self.__profesor
    @property
    def numero(self):
            return self.__numero
    @property
    def hSemanales(self):
        return self.__hSemanales
    @property
    def imagen(self):
        return self.__imagen
        
    #Metodos set
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    @profesor.setter
    def profesor(self,profesor):
        self.__profesor = profesor
    @numero.setter
    def numero(self,numero):
        self.__numero = numero
    @hSemanales.setter
    def hSemanales(self,horas):
        self.__hSemanales = horas
    
    @imagen.setter
    def imagen(self, imagen):
        self.__imagen = imagen