"""
URL configuration for Codo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from .views import IndexPage
from .views import Funcion
from .views import Comentarios
from .views import Login
from .views import Dejar_comentario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPage.as_view(), name="index"),
    path("byFunction", Funcion.as_view(), name="byFunction"),
    path("comentarios", Comentarios.as_view(), name="comentarios"),
    path("login", Login.as_view(), name="login"),
    path("dejar_comentario", Dejar_comentario.as_view(), name="dejar_comentario")
]
