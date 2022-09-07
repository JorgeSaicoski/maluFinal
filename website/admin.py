from django.contrib import admin
from .models import Message, Curriculum

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'create_at')
    search_fields = ('email', 'name', 'id_contact')
# Register your models here.
admin.site.register(Message, MessagesAdmin)
admin.site.register(Curriculum)