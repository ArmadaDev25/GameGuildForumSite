from django.urls import path
from . import views

urlpatterns = [
    path('landing/', views.LandingPage.as_view(), name='landingpage' )
]