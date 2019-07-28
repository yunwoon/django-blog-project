from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.board,name="board"),
    path('detail/<int:blog_id>',views.detail,name="detail"),
    #<int:blog_id> <- path converter(여러 객체를 다루는, 계층적인 URL자동생성 유리)
    #blog_id를 blog.views.detail에 인자로 넘겨준다
    path('new/',views.new,name="new"),
    path('create',views.create,name="create"),
    path('place/',views.place,name="place"),
    #path('어떤 url이 들어오면',(어디에 있는)어떤함수를 실행시켜라)
]