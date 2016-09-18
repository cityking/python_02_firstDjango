"""firstDjamgo URL Configuration

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
from hello import views

urlpatterns = [

    url(r'^hello/$', views.hello),
    url(r'^add_publisher/$', views.add_publisher,name='add_publisher'),
    # url(r'^hello/\d{2}$', views.hello),
    # url(r'^test/(?P<id>\d{2})/$', views.test),
    # url(r'^test1/(?P<id>\d{2})/(?P<key>\w+)/$', views.test1),
]
