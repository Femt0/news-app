from django.contrib import admin

from .models import Article, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    

class AritcleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(Article, AritcleAdmin)
admin.site.register(Comment)
