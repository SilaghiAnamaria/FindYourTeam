from calendar import calendar

from django import forms

from django.forms import TextInput, Select, Textarea, ImageField
from teams.models import Player, Location, Event, Sport


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {

            "nume": TextInput(attrs={'placeholder': "Introduceti numele evenimentului", "class": "form-control"}),
            "oras": Select(attrs={"class": "form-select"}),
            "de_la":TextInput(attrs={'class': 'form-control', 'type': 'date', }),
            "pana_la":TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            "descriere": Textarea(attrs={'placeholder': "Introduceti o descriere a evenimentului", "class": "form-control"}),
            "sporturi": Select(attrs={"class": "form-select"}),
            "dificultate": Select(attrs={"class": "form-select"}),

        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = "__all__"
        widgets = {
            "nume": TextInput(attrs={'placeholder': "Introduceti numele", "class": "form-control"}),
            "prenume": TextInput(attrs={'placeholder': "Introduceti prenumele", "class": "form-control"}),
            "porecla": TextInput(attrs={'placeholder': "Introduceti o porecla (optional)", "class": "form-control"}),
            "varsta": TextInput(attrs={'placeholder': "Introduceti varsta", "class": "form-control"}),
            "oras": TextInput(attrs={'placeholder': "Introduceti localitatea", "class": "form-control"}),
            "gen": Select(attrs={"class": "form-select"}),
            # "poza": ImageField(attrs={'placeholder': "Incarcati poza de profil(optional)", 'class': 'profile-pic'}),
            "descriere": Textarea(attrs={"placeholder": "Faceti-va o descriere", "class": "form-control"}),

        }


class PlayerImageForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['nume', 'poza']



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
        widgets = {
            "nume": TextInput(attrs={'placeholder': "Introduceti numele locatiei", "class": "form-control"}),
            "oras": TextInput(attrs={'placeholder': "Introduceti localitatea", "class": "form-control"}),
            "adresa": TextInput(attrs={'placeholder': "Introduceti adresa", "class": "form-control"}),
            "descriere": Textarea(attrs={"placeholder": "Faceti o descriere a locatiei", "class": "form-control"}),

        }



class SportForm(forms.ModelForm):
    class Meta:
        model = Sport
        fields = '__all__'
        widgets = {
            "nume": TextInput(attrs={'placeholder': "Introduceti numele sportului", "class": "form-control"}),
            "locatie": TextInput(attrs={'placeholder': "Introduceti locatia", "class": "form-control"}),
            "oras": TextInput(attrs={'placeholder': "Introduceti localitatea", "class": "form-control"}),
            "descriere": Textarea(attrs={"placeholder": "Faceti o descriere a sportului", "class": "form-control"}),
            "gen": Textarea(attrs={"class": "form-control"}),
            "numar_minim_de_jucatori": TextInput(attrs={'placeholder': "Introduceti numarul minim de jucatori", "class": "form-control"}),
            "numar_maxim_de_jucatori": TextInput(attrs={'placeholder': "Introduceti numarul maxim de jucatori", "class": "form-control"}),
        }


