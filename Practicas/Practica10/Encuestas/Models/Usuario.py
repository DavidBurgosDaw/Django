class Usuario():
    def __init__(self,nombre,apellidos,edad,sexo,temas,aficiones):
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__edad = edad
        self.__sexo = sexo
        self.__temas = temas
        self._aficiones = aficiones

    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellidos(self):
        return self.__apellidos
    @property
    def edad(self):
        return self.__edad
    @property
    def sexo(self):
        return self.__sexo
    @property
    def temas(self):
        return self.__temas
    @property
    def aficiones(self):
        return self.__aficiones