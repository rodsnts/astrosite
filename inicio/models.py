from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class Post (models.Model):
    title = models.CharField(max_length=255)
    sumary = RichTextField()
    content = RichTextUploadingField() #contem o upload de algum arquivo
    author = models.ForeignKey(User, on_delete = models.PROTECT)  #impede que qualquer um modifique ou exclua o post
    created_at = models.DateField(auto_now_add= True)

    #transformando em string para facilitar a listagem
    def __str__(self):
        return self.title

class Projeto (models.Model):
    title= models.CharField(max_length=250)
    content = RichTextUploadingField() #contem o upload de algum arquivo
    author = models.ForeignKey(User, on_delete = models.PROTECT)  #impede que qualquer um modifique ou exclua o post
    created_at = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title  

class Exoplanetas (models.Model):
    
    title= models.CharField(max_length=250)
    content = RichTextUploadingField() #contem o upload de algum arquivo
    author = models.ForeignKey(User, on_delete = models.PROTECT)  #impede que qualquer um modifique ou exclua o post
    created_at = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title  


class Documentation (models.Model):
    
    title= models.CharField(max_length=250)
    content = RichTextUploadingField() #contem o upload de algum arquivo
    author = models.ForeignKey(User, on_delete = models.PROTECT)  #impede que qualquer um modifique ou exclua o post
    created_at = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title  

class ProgramasGit(models.Model):

    title= models.CharField(max_length=250)
    content = RichTextUploadingField() 
    #contem o upload de algum arquivo
    author = models.ForeignKey(User, on_delete = models.PROTECT)  
    #impede que qualquer um modifique ou exclua o post
    created_at = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title  



        




