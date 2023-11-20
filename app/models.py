from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Img(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nom kiriting")
    body = models.TextField(max_length=100, verbose_name='malumot bering')
    img = models.ImageField(upload_to='images', verbose_name='rasmni yuklang')

    def __str__(self):
        return self.title
    

class AboutMe(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title