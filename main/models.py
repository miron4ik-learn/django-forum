from django.db import models
from django.urls import reverse

class Post(models.Model):
  title = models.CharField(verbose_name='Название поста', max_length=100)
  description = models.TextField(verbose_name='Описание', null=True, blank=True)
  image = models.ImageField(verbose_name='Картинка', null=True, blank=True)
  created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
  updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
  
  def get_absolute_url(self):
    return reverse('home')
  
  def __str__(self):
    return self.title
  
class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  description = models.TextField(verbose_name='Описание', null=True, blank=True)
  created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
  
  def get_absolute_url(self):
    return reverse('home')
  
  def __str__(self):
    return self.description