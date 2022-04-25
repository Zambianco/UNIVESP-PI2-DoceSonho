"""DoceSonho URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.urls import re_path
from . import views
from Portfolio import views as Portfolio
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('views/', views.index, name='index'), ##use react for index
    re_path('views/'r'^$', views.index, name='index'),
    path('admin/', admin.site.urls), #Painel administrativo do site
    path('listBolo/', Portfolio.listBolo),
    path('listDoce/', Portfolio.listDoce),
    path('bolos/', Portfolio.bolo_show),
    path('listQuitute/', Portfolio.listQuitute),
    path('listCategoria/', Portfolio.listCategoria),
    path('',include('frontend.urls')),

    #===== Registro, login e logout de usuários =====
    path("register/", views.register_request, name="register"), #Pagina de registro dos usuários do site
    path("login", views.login_request, name="login"), #Página de login dos usuários do site
    path("logout", views.logout_request, name= "logout"), #Página de logout dos usuários do site

    #===== Recuperação de senha de usuários =====
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset")

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
