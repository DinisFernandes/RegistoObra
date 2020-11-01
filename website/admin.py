from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'data_post',)
    list_display_links = ('id', 'title')


admin.site.register(Post, PostAdmin)