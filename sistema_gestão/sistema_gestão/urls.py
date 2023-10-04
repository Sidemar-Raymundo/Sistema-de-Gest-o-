"""
URL configuration for sistema_gestão project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib import admin
from django.urls import path
from app_gestao import views
from usuarios import views as usuario_views
from django.contrib.auth import views as auth_view




urlpatterns = [
    path('conta/',usuario_views.novo_usuario,name='novo_usuario'),
    path('login/',auth_view.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='usuarios/logout.html'),name='logout'),

    path('admin/', admin.site.urls),
    path('',views.itens,name='itens'),
    path('novo_item/',views.criar, name='novo_item'), 
    path('novo_item/<int:id_itens>',views.editar,name= 'editar'),
    path('/<int:id_itens>',views.detalhe,name='detalhe'),
    path('excluir_item/<int:id_itens>',views.excluir,name='excluir')
    
    
]
