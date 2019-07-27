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
from django.urls import path, include
import blog.views
import portfolio.views
import accounts.views
from django.conf import settings #media 파일을 쓰기 위함 111
from django.conf.urls.static import static #media 파일을 쓰기 위함 222

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.index,name="index"),
    path('board/',include('blog.urls')),
    path('portfolio/',portfolio.views.portfolio,name="portfolio"),
    path('accounts/',include('accounts.urls')), #allauth 와 accounts 대 혼 란
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #MEDIA 를 더하는거임

# 바로 위에 static 한거랑 같게 따로 쓰고 싶으면
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 이렇게도 쓸 수 있음