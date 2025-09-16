from django.contrib import admin
from .models import Article, ContactMessage

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "is_published", "created_at")
    search_fields = ("title", "content")
    list_filter = ("is_published",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "satisfaction", "satisfaction_score", "created_at")
    search_fields = ("name", "email", "message")
    list_filter = ("satisfaction",)


