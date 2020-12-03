from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('dreamreal/', views.dreamreal, name='dreamreal'),
    path('create/',views.create,name = 'create'),
    path('save_book1/',views.save_book1,name = 'save_book1')
]

