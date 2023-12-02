from django.shortcuts import render
from .models import GuildInfo
from django.views.generic.base import RedirectView
from django.views.generic import DetailView
# Create your views here.

class LandingPage(DetailView):
    model = GuildInfo
    template_name = "landingpage.html"

class LandingPageRedirect(RedirectView):
    permanent = True