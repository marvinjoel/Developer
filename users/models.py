from distutils.command.upload import upload

from django.db import models


# TODO: Poner los link, campo no obligatorio
class DetailsModel(models.Model):
    email = models.EmailField(verbose_name='Email', max_length=300, blank= True, null=True)
    repo = models.CharField(verbose_name='Repositorio', max_length=500, blank= True, null=True)
    linkedin = models.CharField(verbose_name='LinkedInd', max_length=500, blank= True, null=True)
    twitter = models.CharField(verbose_name='Twitter', max_length=500, blank= True, null=True)
    instagram = models.CharField(verbose_name='Instagram', max_length=500, blank= True, null=True)
    portfolio = models.CharField(verbose_name='Portafolio', max_length=500, blank= True, null=True)
    valoration = models.IntegerField(verbose_name='valoración', blank= True, null=True)

    def __str__(self):
        return self.email

    
    class Meta:
        verbose_name = 'DetailsModel'
        verbose_name_plural = 'DetailsModels'
        ordering = ['id']


# Personal Data
class UserModel(models.Model):
    first_name = models.CharField(verbose_name='Nombres', max_length=200)
    last_name = models.CharField(verbose_name='Apellidos', max_length=200)
    photo = models.ImageField(verbose_name='Foto',upload_to='user/%Y/%m/%d',default='img/user.jpg', blank=True, null=True)
    detail = models.ForeignKey(DetailsModel, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'UserModel'
        verbose_name_plural = 'UserModels'
        ordering = ['id']
