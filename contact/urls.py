from django.urls import path 

from . import views 

urlpatterns = [
   path('', views.contact_list, name='contact_list'),
   path('create/', views.contact_create, name='contact_create'),
   path('<int:id>/', views.contact_detail,name='contact_detail'),
   path('update/<int:id>/', views.contact_update,name='contact_update'),
   path('delete/<int:id>/', views.contact_delete,name='contact_delete'),

   
]