from django.contrib import admin

from .models import Achievement, AchievementCat, Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner')
    list_filter = ('color', 'birth_year')
    search_fields = ('name', 'owner__username')
    raw_id_fields = ('owner',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(AchievementCat)
class AchievementCatAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'cat')
