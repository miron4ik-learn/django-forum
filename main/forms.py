from django.forms import ModelForm
from . import models

class PostForm(ModelForm):
  class Meta:
    model = models.Post
    fields = '__all__'

class CommentForm(ModelForm):
  class Meta:
    model = models.Comment
    fields = [ 'description' ]