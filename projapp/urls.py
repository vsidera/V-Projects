from django.urls import path
from . import views
from .views import (PostDetailView,PostUpdateView,PostDeleteView)

urlpatterns = [
    path('', views.home, name='projapp-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.new_post, name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]