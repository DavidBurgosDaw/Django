from django.shortcuts import render
from django.utils.timezone import now
from perfilusuario.forms import FrmLogin
from perfilusuario.models import Usuario

def home(request):
    mensaje = ""

    if request.method == 'POST':
        form = FrmLogin(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            password = form.cleaned_data['password']

            usuario = buscar_usuario(nickname)

            if usuario is None:
                mensaje = "Usuario no encontrado"
            elif usuario.password != password:  # Comparación directa
                mensaje = "Contraseña incorrecta"
            else:
                # Actualizar la fecha de último acceso
                usuario.ultimo_acceso = now()
                usuario.save()

                return render(request, 'perfilusuario/bienvenida.html', {'usuario': usuario})

    else:
        form = FrmLogin()

    return render(request, 'perfilusuario/base.html', {'form': form, 'mensaje': mensaje})

# Función para buscar un usuario por su nickname
def buscar_usuario(nickname):
    try:
        return Usuario.objects.get(nickname=nickname)
    except Usuario.DoesNotExist:
        return None
