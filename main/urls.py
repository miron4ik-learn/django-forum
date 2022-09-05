from django.urls import path
from . import views

urlpatterns = [
  path('', views.PostsView.as_view(), name='home'),
  
  path('post/<int:pk>', views.DetailPostView.as_view(), name='detail_post'),
  path('post/<int:pk>/add-comment', views.AddCommentView.as_view(), name='add_comment'),
  
  path('create-post', views.CreatePostView.as_view(), name='create_post'),
  path('update-post/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
  path('delete-post/<int:pk>', views.DeletePostView.as_view(), name='delete_post'),
  
  path('about', views.about, name='about'),
]