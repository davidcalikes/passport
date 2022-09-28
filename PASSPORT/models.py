from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


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


class Profile(models.Model):
    my_profile_image = CloudinaryField(
        'image',
        default='placeholder')
    my_name = models.CharField(
        max_length=200,)
    my_emergency_contact_one_name = models.CharField(
        max_length=200, default='')
    my_emergency_contact_one_number = models.PositiveIntegerField(
        default=0,)
    slug = models.SlugField(
        max_length=200, unique=True, default='')
    my_emergency_contact_two_name = models.CharField(
        max_length=200, default='')
    my_emergency_contact_two_number = models.PositiveIntegerField(
        default=0,)
    my_date_of_birth = models.DateField(
        default='DD/MM/YY')
    my_biography = models.TextField(
        max_length=600, blank=False)
    my_family = models.TextField(
        max_length=600, blank=False)
    my_likes = models.TextField(
        max_length=600, blank=False)
    my_dislikes = models.TextField(
        max_length=600, blank=False)
    my_strengths = models.TextField(
        max_length=600, blank=False)
    my_difficulties = models.TextField(
        max_length=600, blank=False)
    my_supports = models.TextField(
        max_length=600, blank=False)
    my_calming_measures = models.TextField(
        max_length=600, blank=False)
    my_communication_skills = models.TextField(
        max_length=600, blank=False)
    my_other_info = models.TextField(
        max_length=600, blank=False)
    my_family_image = CloudinaryField(
        'image',
        default='placeholder')
    my_hobby_image = CloudinaryField(
        'image',
        default='placeholder')
    my_additional_image = CloudinaryField(
        'image',
        default='placeholder')
    approved = models.BooleanField(
        default=False)

    def __str__(self):
        return self.my_name
