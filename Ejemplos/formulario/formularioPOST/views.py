from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#@csrf_exempt
def homePOST(request):
    if request.method=="POST":
        nombre=request.POST['nombre']
        email=request.POST['email']
        texto=request.POST['texto']
        return render(request,'saludo_post.html',locals())
    else:
        return render(request,"homepost.html")