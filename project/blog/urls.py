from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.board,name="board"),
    path('detail/<int:blog_id>',views.detail,name="detail"),
    path('new/',views.new,name="new"),
    path('create',views.create,name="create"),
    path('newblog/',views.blogpost,name="newblog"),
    path('place/',views.place,name="place"),
    #path('어떤 url이 들어오면',(어디에 있는)어떤함수를 실행시켜라)
]