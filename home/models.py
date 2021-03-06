from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField


# Create your models here.
#

class Language(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    img = models.ImageField(default='default.jpg',verbose_name="Imagen",upload_to='lan_pics')
    active = models.BooleanField(default=False)  # van a ser verdaderos cuando quiera mostrarlos

    def __str__(self):
        return self.name


class Sentence(models.Model):
    name= models.CharField(max_length=50,verbose_name="Nombre")
    def __str__(self):
        return self.name

class SyntaxPost(models.Model):
    #content = models.TextField(max_length=3000,verbose_name="Contenido")
    content = RichTextField(max_length=3000,verbose_name="Contenido",config_name='special')
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    author = models.ForeignKey(User, verbose_name="Autor",blank=True,on_delete=models.SET_NULL,null=True)
    sentence = models.ForeignKey(Sentence, verbose_name="sentencia",on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name="lenguaje",on_delete=models.CASCADE)
    active = models.BooleanField(default=False)  # van a ser verdaderos cuando quiera mostrarlos

    def __str__(self):
        return str(self.content)

class Marker(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    post = models.ForeignKey(SyntaxPost, verbose_name="Post",on_delete=models.CASCADE)
    #def __str__(self):
    #    return str(self.user.get_username(),self.post.content)

class Suggestion(models.Model):
    langName = models.CharField(max_length=30, verbose_name="Nombre del Lenguaje")
    langVer = models.CharField(max_length=30, verbose_name="Version del Lenguaje")
    website = models.CharField(max_length=50, verbose_name="Página Oficial")
    comments = RichTextField(max_length=3000, verbose_name="Descripcion")

class Contact(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    email = models.EmailField(max_length=30, verbose_name="Email")
    mensaje = RichTextField(max_length=3000, verbose_name="Tu mensaje")

class Report(models.Model):
    RESOLVED = 'Y'
    UNRESOLVED = 'N'
    RESOLVED_CHOISES = (( RESOLVED,'YES'),(UNRESOLVED,'NO'))
    user = models.ForeignKey(User,verbose_name="Autor",null=True,blank=True,on_delete=models.CASCADE)
    post = models.ForeignKey(SyntaxPost,verbose_name="Post",on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Report creado")
    description= models.TextField(max_length=5000,verbose_name="descripción")
    resolved = models.CharField(max_length=2,choices=RESOLVED_CHOISES,default='N')
    def __str__(self):
        return self.description[:10]

