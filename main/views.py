from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models
from . import forms

def about(request):
  return render(request, 'about.html')

class PostsView(ListView):
  model = models.Post
  template_name = 'home.html'
  ordering = [ '-created_at' ]
  
class DetailPostView(DetailView):
  model = models.Post
  template_name = 'detail_post.html'
  
class CreatePostView(CreateView):
  model = models.Post
  template_name = 'create_post.html'
  form_class = forms.PostForm
  
class UpdatePostView(UpdateView):
  model = models.Post
  template_name = 'update_post.html'
  form_class = forms.PostForm
  
class DeletePostView(DeleteView):
  model = models.Post
  template_name = 'delete_post.html'
  success_url = reverse_lazy('home')
  
class AddCommentView(CreateView):
  model = models.Comment
  template_name = 'add_comment.html'
  form_class = forms.CommentForm
  
  def form_valid(self, form):
    form.instance.post_id = self.kwargs['pk']
    return super().form_valid(form)