from django import forms


class modelBlogForm(forms.Form):

    titulo = forms.CharField(max_length=70)
    subtitulo = forms.CharField(max_length=280)
    seccion = forms.CharField(max_length=70)
    contenido = forms.CharField(max_length=1120)
    autor = forms.CharField(max_length=70)
    fecha = forms.DateField()
    # imagen = forms.ImageField()
