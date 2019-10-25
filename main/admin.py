from django.contrib import admin

# Register your models here.

from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'middle_name',
    )


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
    )


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)