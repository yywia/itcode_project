from django.contrib import admin
from Fog import models

# Register your models here.
@admin.register(models.Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'price')

@admin.register(models.Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(models.Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('author', 'game', 'text', 'is_recommended', 'score')

@admin.register(models.Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('game','review_score', 'review_amount')