from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Profile


class ProfilesList(generic.ListView):
    """
    Displays list of pupil profiles
    """
    model = Profile
    template_name = 'list.html'
    context_object_name = 'profile_list'


class PupilProfile(View):
    """
    Displays pupil profile selected by authenticated user
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Gets selected profile
        """
        queryset = Profile.objects.filter()
        pupil = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'profile.html',
            {
                "pupil": pupil,
            },
        )
