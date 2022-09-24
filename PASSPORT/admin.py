from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import EnrolledPupil


@admin.register(EnrolledPupil)
class EnrolledPupilAdmin(SummernoteModelAdmin):
    list_display = ['pupil_first_name', 'pupil_last_name',
                    'school_name', 'teacher_name', 'school_roll_no',
                    'pupil_id']
    summernote_fields = ('content')
