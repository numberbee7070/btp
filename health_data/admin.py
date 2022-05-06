from django.contrib import admin
from .models import HealthRecord


class HealthAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "temperature",
        "height",
        "weight",
        "created_at",
        "school",
    )

    def school(self, obj):
        return obj.student.school


admin.site.register(HealthRecord, HealthAdmin)
