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
            elif not usuario.verificar_password(password):  # Comprobamos con `check_password`
                mensaje = "Contraseña incorrecta"
            else:
                usuario.ultimo_acceso = now()
                usuario.save()

                return render(request, 'perfilusuario/bienvenida.html', {'usuario': usuario})

    else:
        form = FrmLogin()

    return render(request, 'perfilusuario/base.html', {'form': form, 'mensaje': mensaje})

def buscar_usuario(nickname):
    """ Busca un usuario en la base de datos """
    try:
        return Usuario.objects.get(nickname=nickname)
    except Usuario.DoesNotExist:
        return None
