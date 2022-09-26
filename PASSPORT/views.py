from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import EnrolledPupil


class PupilsList(generic.ListView):
    """
    Displays list of enrolled pupils
    """
    model = EnrolledPupil
    template_name = 'list.html'
    context_object_name = 'pupil_list'
