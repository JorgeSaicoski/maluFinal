from django.contrib import admin
from .models import Project, Category, Image


class ImagesInLine(admin.StackedInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    list_editable = ('category',)
    inlines = [ImagesInLine,]

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    list_editable = ('project',)

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)

admin.site.site_header = "Malu Admin"
admin.site.site_title = "Admin Malu"
admin.site.index_title = "Painel de Administracao"
