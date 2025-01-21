class Persona:
    def __init__(self, nombre, edad, ciudad):
        # Atributos de la persona
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}."
    
    def cumpleaños(self):
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tienes {self.edad} años."
