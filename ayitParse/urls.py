"""ayitParse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django_web.views import import_json_info
from django_web.views import science_json_info
from django_web.views import trends_json_info
from django_web.views import affiche_json_info

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/affiche/', affiche_json_info),
    url(r'^json/import/', import_json_info),
    url(r'^json/science/', science_json_info),
    url(r'^json/trends/', trends_json_info)
]
