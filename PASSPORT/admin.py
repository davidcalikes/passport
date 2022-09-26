from django.contrib import admin
from .models import EnrolledPupil


@admin.register(EnrolledPupil)
class EnrolledPupilAdmin(admin.ModelAdmin):
    list_display = ('pupil_first_name', 'pupil_last_name',
                    'school_name', 'teacher_name', 'school_roll_no',
                    'pupil_id')
    search_fields = ('pupil_last_name', 'school_name')
    actions = ['approved_entry']

    def approved_entry(self, request, queryset):
        queryset.update(approved=True)
