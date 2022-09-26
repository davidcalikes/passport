from django import forms
from .models import EnrolledPupil


class UploadPupilForm(forms.ModelForm):

    """
    Form for recipe review
    """
    class Meta:
        """
        Form has field of body from Review model
        """
        model = EnrolledPupil
        fields = (
            'pupil_last_name', 'pupil_first_name', 
            'school_name', 'teacher_name', 'school_roll_no',
            'pupil_id', 'approved', )
