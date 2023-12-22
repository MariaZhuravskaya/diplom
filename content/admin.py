from django.contrib import admin

from content.models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'date_creation', 'date_change',
                    'author', 'is_publication', 'price', 'paid')
    search_fields = ('name', 'description')



