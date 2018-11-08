"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#coding: utf-8
from django.conf.urls import url

from blog.views import PostsListView, PostDetailView

urlpatterns = [
                       url(r'^$', PostsListView.as_view(), name='list'),
                       # то есть по URL http://имя_сайта/blog/
                       # будет выводиться список постов
                       
                       url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
                       
                       # по URL http://имя_сайта/blog/число/
                       # будет выводиться пост с определенным номером
                       
                       ]
