from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, default="")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Project(models.Model):
    name = models.CharField(max_length=30, null=False, default="", unique=True)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey('Category',default=1, on_delete=models.SET_DEFAULT ,related_name="created")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

class Image(models.Model):
    name = models.CharField(max_length=30, default="")
    url = models.ImageField(upload_to='images/', blank=True)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name="created")
    #Dont return the __str__. It bug the views
    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"


