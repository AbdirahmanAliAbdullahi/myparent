"""myparent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from . import views



urlpatterns = [
    path('',PostListView.as_view(),name='blog-home' ),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts' ),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail' ),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update' ),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete' ),
    path('post/new/',PostCreateView.as_view(),name='post-create' ),
    path('about/',views.about,name='blog-about' ),
]
