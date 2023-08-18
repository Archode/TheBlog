from django.urls import path
from .views import HomeView, ArticleDetailView, CreatePostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
from . import views

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(), name='article-detail'),
    path('createpost/',CreatePostView.as_view(),name='create_post'),
    path('updatepost/<int:pk>/',UpdatePostView.as_view(),name='update_post'),
    path('deletepost/<int:pk>',DeletePostView.as_view(),name='delete_post'),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('add_category/',AddCategoryView.as_view(),name='add_category'),
    path('category/<str:cats>/',views.CategoryView, name='category'),


]