from django.contrib import admin
from personne_app.models import Personne


@admin.register(Personne)
class PersonneAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birthday')
    search_fields = ('last_name', 'first_name', 'birthday')
