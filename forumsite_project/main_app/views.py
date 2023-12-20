from django.shortcuts import render
from .models import GuildInfo
from django.views.generic.base import RedirectView
from django.views.generic import DetailView

# User Login/Registration imports
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Auth Requirement Imports
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.



class LandingPageRedirect(RedirectView):
    permanent = True