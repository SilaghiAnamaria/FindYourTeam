from calendar import calendar

from django import forms

from django.forms import TextInput, Select, Textarea, ImageField, DateInput
from teams.models import Player, Location, Event, Sport


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = "__all__"
        widgets = {

            "nume": TextInput(attrs={'placeholder': "Introduceti numele evenimentului", "class": "form-control"}),
            "oras": Select(attrs={"class": "form-select"}),
            "de_la":DateInput(attrs={"type": "datetime-local", "class": "form-control"}, format="%Y-%m-%dT%H:%M"),
            "pana_la":DateInput(attrs={"type": "datetime-local", "class": "form-control"}, format="%Y-%m-%dT%H:%M"),
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
            "gen": Select(attrs={"class": "form-control"}),
            "numar_minim_de_jucatori": TextInput(attrs={'placeholder': "Introduceti numarul minim de jucatori", "class": "form-control"}),
            "numar_maxim_de_jucatori": TextInput(attrs={'placeholder': "Introduceti numarul maxim de jucatori", "class": "form-control"}),
        }


# class EventForm(ModelForm):
# class Meta:
    #     model = Event
    #     fields = "__all__"
    #     # datetime-local is a HTML5 input type
    #     widgets = {
    #         "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter event title"}),
    #         "description": forms.Textarea(attrs={"class": "form-control","placeholder": "Enter event description"}),
    #         "start_time": DateInput(attrs={"type": "datetime-local", "class": "form-control"}, format="%Y-%m-%dT%H:%M"),
    #         "end_time": DateInput(attrs={"type": "datetime-local", "class": "form-control"}, format="%Y-%m-%dT%H:%M"),
    #     }
    #     # exclude = ["user"]

    #
    # def __init__(self, *args, **kwargs):
    #     super(EventForm, self).__init__(*args, **kwargs)
    #     # input_formats to parse HTML5 datetime-local input to datetime field
    #     self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
    #     self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)

#     class Meta:
#         model = Event
#         fields = ["title", "description", "start_time", "end_time"]
#         # datetime-local is a HTML5 input type
#         widgets = {
#             "title": forms.TextInput(
#                 attrs={"class": "form-control", "placeholder": "Enter event title"}
#             ),
#             "description": forms.Textarea(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Enter event description",
#                 }
#             ),
#             "start_time": DateInput(
#                 attrs={"type": "datetime-local", "class": "form-control"},
#                 format="%Y-%m-%dT%H:%M",
#             ),
#             "end_time": DateInput(
#                 attrs={"type": "datetime-local", "class": "form-control"},
#                 format="%Y-%m-%dT%H:%M",
#             ),
#         }
#         exclude = ["user"]
#
#     def __init__(self, *args, **kwargs):
#         super(EventForm, self).__init__(*args, **kwargs)
#         # input_formats to parse HTML5 datetime-local input to datetime field
#         self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
#         self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


# class AddMemberForm(forms.ModelForm):
#     class Meta:
#         model = EventMember
#         fields = ["user"]