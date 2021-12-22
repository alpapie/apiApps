from django.urls import path

from . import views

urlpatterns = [
    path('', views.connect, name='index'),
    path('contact', views.page, name='contact'),
     
    path('detail/<int:id_detail>', views.detail, name='detail'),
     
    path('delete/<int:id_sup>', views.delette, name='delette'),
    
    path('modifpage', views.modifpage, name='modifpage'),
    path('modifaction', views.modifAction, name='modifAction'),
    
    path('ajoutform', views.ajoutcontact, name='ajoutform'),
    
    path('deconnection', views.deconnection, name='deconnection'),
     
    path('test', views.test, name='test'),
    
]