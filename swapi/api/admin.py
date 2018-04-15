from django.contrib import admin

from api.models import People, Planet


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    pass


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    pass
