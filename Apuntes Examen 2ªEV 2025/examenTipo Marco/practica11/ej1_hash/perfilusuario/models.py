from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now

class Usuario(models.Model):
    nickname = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=128)  # Hash almacenado
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    ultimo_acceso = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        """ Encripta la contraseña antes de guardarla. """
        if not self.password.startswith('pbkdf2_sha256$'):  # Evita doble encriptado
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def verificar_password(self, password):
        """ Verifica si la contraseña ingresada es correcta. """
        return check_password(password, self.password)
