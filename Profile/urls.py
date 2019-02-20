"""TOURISM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from Profile import views
from django.contrib.auth.views import login , logout

urlpatterns = [
        url(r'^[A-Za-z\- / A-Za-z\-]+/signup/$', views.addUser , name='signup'),  ### visitor moved from home to register
        url(r'^[A-Za-z\- / A-Za-z\-]+/signin/$', login , {'template_name' : 'login.html'}),
        url(r'^[A-Za-z\- / A-Za-z\-]+/logout/$', logout),
        url(r'^[A-Za-z\- / A-Za-z\-]+/profile/$', views.viewAccount),

        # url(r'^home$', views.temphome),
]


