"""
URL configuration for kardex_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from kardex import views as kardex_views
from django.contrib.auth.decorators import user_passes_test
from usuarios import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', usuario_views.registro_view, name='registro'),
    path('login/', usuario_views.login_view, name='login'),
    path('logout/', usuario_views.logout_view, name='logout'),
    path('', kardex_views.kardex_view, name='kardex'),
    path('agregar-compra/', kardex_views.agregar_compra, name='agregar_compra'),
    path('admin/kardex/', 
         user_passes_test(lambda u: u.is_superuser)(kardex_views.admin_kardex_view), 
         name='admin_kardex'),
    path('admin/kardex/', user_passes_test(lambda u: u.is_superuser)(kardex_views.admin_kardex_view), name='admin_kardex'),
]