from django.urls import path
from . import views

urlpatterns = [
   path('', views.book_list, name='book_list'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('members/', views.member_list, name='member_list'),
    path('add-book/', views.add_book, name='add_book'),

]