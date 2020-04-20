"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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


from django.conf.urls.static import static
from django.conf import settings
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('', views.home),
    path('posts/<int:post_id>', views.post),
    path('home/',views.home),
    path('sobre_o_projeto/',views.sobre_o_projeto),
    path('exoplanetas/',views.exoplanetas),
    path('documentacao/',views.documentation),
    path('livro/',views.livro),
    path('programas-git/',views.programasgit)



]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT) #quando acessar media apontará para a propria pasta dentro do app
