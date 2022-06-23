from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from instagram.models import Post, Comment

# admin.site.register(Post)

# class PostAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post, PostAdmin)

@admin.register(Post) #Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length','is_public', 'created_at', 'updated_at',]
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message'] # messsage 기준으로 필터를 생성 한다. Post.objects.all().filter([개체]__[속성]='검색할 문자열')

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" width="75px"/>')
        return None

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass