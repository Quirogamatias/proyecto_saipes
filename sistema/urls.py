"""sistema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.views.static import serve
from django.urls import path,include,re_path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import Inicio,Login,logoutUsuario

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include(('apps.usuario.urls','usuarios'))),
    path('institucion/',include(('apps.institucion.urls','institucion'))),
    path('',Inicio.as_view(),name= 'index'),
    path('accounts/login/',Login.as_view(), name= 'login'),
    path('logout/',login_required(logoutUsuario),name= 'logout'),
    
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
