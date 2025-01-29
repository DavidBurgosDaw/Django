from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(max_length=5,required=True,widget=forms.TextInput(attrs= {'class':'form-control','placeholder':"Tu nombre"}),label="Nombre")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'ejemplo@ejemplo.com'}),label="Email")
    fecha=forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control'},years=range(1900,2002)))
    SEXO=[('mujer','Femenino'),
         ('hombre','Masculino')]
    sexo=forms.ChoiceField(choices=SEXO,widget=forms.RadioSelect)
    mensaje=forms.CharField(widget=forms.Textarea(attrs={'rows':6,'class':'form-control'}), initial="Dinos lo que piensas")
    autorizacion=forms.CharField(required=False, widget=forms.CheckboxInput,label="Autorizo el tratamiento de mis datos")

    #Este checkbox es para cuando ponemos uno sólo, también podemos usar ChoiceFiel. por defecto su valor es requerido por lo
    #que si no lo clikeamos no pasaremos la validación
    #Si queremos poner varios checkbox tenemos que usar MultipleChoiceField con el widget CheckboxSelectMultiple
    #Si queremos usar una lista(select) ChoiceField con widget select
    
    """  
  nombre=forms.CharField(max_length=4,required=True)      
    email=forms.EmailField(max_length=25,required=True)
    #fecha=forms.DateField()
    mensaje=forms.CharField(max_length=100,required=True)
    """
    
 
    
        
    
    