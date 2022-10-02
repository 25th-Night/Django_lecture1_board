"""config URL Configuration

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
from django.urls import path
from board.views import (
    IndexClass,
    IndexClass2,
    index_function,
    index_function2,
    index_function3,
    index_function4,
    index_function5,
)

urlpatterns = [
    # 127.0.0.1:8000/admin/ 으로 접속 시, admin page 나옴
    path("admin/", admin.site.urls),
    # 127.0.0.1:8000/ 으로 접속 시, views.py에서 생성한 index_function 을 통해 처리한 방법대로 화면이 나옴
    path("fbv/", index_function, name="index_function"),
    path("cbv/", IndexClass.as_view(), name="index_class"),
    path("fbv2/", index_function2, name="index_function2"),
    path("fbv3/", index_function3, name="index_function3"),
    path("fbv4/<str:name>/<str:code>/", index_function4, name="index_function4"),
    path("cbv2/", IndexClass2.as_view(), name="index_class2"),
    path("fbv5/<str:name>/", index_function5, name="index_function5"),
]
