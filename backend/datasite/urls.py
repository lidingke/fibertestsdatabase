"""datasite URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
# import xadmin
# from django.contrib import admin

from apps.producer.views import ResultListViewSet,ResultColumnsListViewSet

router = DefaultRouter()
# router.register(r'goods', GoodsListViewSet, base_name="goods")
router.register(r'producer', ResultListViewSet, base_name="producer")
# router.register(r'producercolumns', ResultColumnsListViewSet, base_name="producercolumns")

urlpatterns = [
    # url(r'^producer/', include('polls.urls')),
    url(r'^', include(router.urls)),
    # url(r'^xadmin/', xadmin.site.urls),
    url(r'^admin/',admin.site.urls)

]
