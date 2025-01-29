class Asignatura():
    
    def __init__(self,nombre,profesor,horas,aula):
        self.__nombre=nombre
        self.__profesor=profesor
        self.__horas=horas
        self.__aula=aula
        
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def profesor(self):
        return self.__profesor
    
    @property
    def horas(self):
        return self.__horas
    
    @property
    def aula(self):
        return self.__aula