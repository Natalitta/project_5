from django.contrib import admin
from .models import Course, Category


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'is_open',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Course, CourseAdmin)
admin.site.register(Category, CategoryAdmin)
