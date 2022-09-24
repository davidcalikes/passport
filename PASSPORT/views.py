from django.views import generic
from .models import EnrolledPupil


class PupilsList(generic.TemplateView):
    model = EnrolledPupil
    template_name = 'index.html'
