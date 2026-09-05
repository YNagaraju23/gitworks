from django.contrib import admin
from .models import createTable, Book
admin.site.register(createTable)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_filter = ('title', 'author')
# Register your models here.
