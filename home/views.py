from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from teams.models import Event


class HomeTemplateView(TemplateView):
    template_name = "home/home.html"


