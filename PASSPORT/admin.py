from django.contrib import admin
from .models import EnrolledPupil, Profile


@admin.register(EnrolledPupil)
class EnrolledPupilAdmin(admin.ModelAdmin):
    list_display = ('pupil_first_name', 'pupil_last_name',
                    'school_name', 'teacher_name', 'school_roll_no',
                    'pupil_id')
    search_fields = ('pupil_first_name', 'pupil_last_name',
                     'school_name', 'teacher_name', 'school_roll_no',
                     'pupil_id')
    actions = ['approved_entry']

    def approved_entry(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('my_emergency_contact_one_number',)}
    list_display = ('my_profile_image', 'my_name',
                    'my_emergency_contact_one_name',
                    'my_emergency_contact_one_number',
                    'my_emergency_contact_two_name',
                    'my_emergency_contact_two_number',
                    'my_date_of_birth', 'my_biography',
                    'my_family', 'my_likes', 'my_dislikes',
                    'my_strengths', 'my_difficulties', 'my_supports',
                    'my_calming_measures', 'my_communication_skills',
                    'my_other_info', 'my_family_image', 'my_hobby_image',
                    'my_additional_image')

    search_fields = ('my_profile_image', 'my_name',
                     'my_emergency_contact_one_name',
                     'my_emergency_contact_one_number',
                     'my_emergency_contact_two_name',
                     'my_emergency_contact_two_number',
                     'my_date_of_birth', 'my_biography',
                     'my_family', 'my_likes', 'my_dislikes',
                     'my_strengths', 'my_difficulties', 'my_supports',
                     'my_calming_measures', 'my_communication_skils',
                     'my_other_info', 'my_family_image', 'my_hobby_image',
                     'my_additional_image')
    actions = ['approved_entry']

    def approved_entry(self, request, queryset):
        queryset.update(approved=True)
