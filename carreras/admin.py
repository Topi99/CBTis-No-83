from django.contrib import admin
from .models import Carrera, Modulo, SubModulo
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(Carrera, MarkdownModelAdmin)
admin.site.register(Modulo)
admin.site.register(SubModulo, MarkdownModelAdmin)
