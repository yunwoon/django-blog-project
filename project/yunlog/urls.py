"""yunlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import blog.views
import portfolio.views
from django.conf import settings #media 파일을 쓰기 위함 111
from django.conf.urls.static import static #media 파일을 쓰기 위함 222

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.index,name="index"),
    path('board/',blog.views.board,name="board"),
    path('board/detail/<int:blog_id>',blog.views.detail,name="detail"),
    path('board/new/',blog.views.new,name="new"),
    path('board/create',blog.views.create,name="create"),
    #path('어떤 url이 들어오면',(어디에 있는)어떤함수를 실행시켜라)
    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #MEDIA 를 더하는거임

# 바로 위에 static 한거랑 같게 따로 쓰고 싶으면
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 이렇게도 쓸 수 있음