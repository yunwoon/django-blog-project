from django.contrib import admin
from .models import Blog, Android, Java
# Register your models here.

admin.site.register(Blog) #admin 사이트에 등록해라
admin.site.register(Android)
admin.site.register(Java)