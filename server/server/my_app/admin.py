from django.contrib import admin
from .models import MyModal
# Register your models here.
class MyModalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
admin.site.register(MyModal, MyModalAdmin)