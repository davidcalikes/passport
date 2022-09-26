from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class EnrolledPupil(models.Model):
    pupil_last_name = models.CharField(
        max_length=200, default='')
    pupil_first_name = models.CharField(
        max_length=200, default='')
    school_name = models.CharField(
        max_length=200, default='')
    teacher_name = models.CharField(
        max_length=200, default='')
    school_roll_no = models.CharField(
        max_length=200, default='')
    pupil_id = models.PositiveIntegerField(
        default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(999999)],
        unique=True)
    approved = models.BooleanField(
        default=False)

    def __str__(self):
        return self.pupil_first_name
