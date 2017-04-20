from django.contrib import admin
from .models import Articulo
from django_markdown.admin import MarkdownModelAdmin

class ArticuloAdmin(MarkdownModelAdmin):
    prepopulated_fields = {"slug": ("nombre",)}
    
admin.site.register(Articulo, ArticuloAdmin)