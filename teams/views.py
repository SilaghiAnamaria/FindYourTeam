from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from teams.forms import EventForm, LocationForm, PlayerForm, SportForm
from teams.models import Event, Player, Location, Sport


class HomeTemplateView(TemplateView):
    template_name = "home/home.html"

class EventCreateView(CreateView):
    template_name = "event/create_event.html"
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("list_of_events")  # unde se duce dupa ce dam submit
    # permission_required = 'echipa.add_echipa'


class EventListView(ListView):
    template_name = "event/list_of_events.html"
    model = Event
    context_object_name = "all_events"
    # permission_req


class EventUpdateView(UpdateView):
    template_name = 'event/update_event.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('list_of_events')




class EventDeleteView(DeleteView):
    template_name = 'event/delete_event.html'
    model = Event
    success_url = reverse_lazy('list_of_events')




class PlayerCreateView(CreateView):
    template_name = "player/create_player.html"
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy("list_of_players")  # unde se duce dupa ce dam submit
    # permission_required = 'jucator.add_jucator'


class PlayerListView(ListView):
    template_name = "player/list_of_players.html"
    model = Player
    context_object_name = "all_players"
    # permission_required = 'jucator.add_jucator'

class PlayerUpdateView(UpdateView):
    template_name = 'player/update_player.html'
    model = Player
    form_class = PlayerForm
    success_url = reverse_lazy('list_of_players')




class PlayerDeleteView(DeleteView):
    template_name = 'player/delete_player.html'
    model = Player
    success_url = reverse_lazy('list_of_players')



class LocationCreateView(CreateView):
    template_name = "location/create_location.html"
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy("list_of_locations")  # unde se duce dupa ce dam submit
    # permission_required = 'locatie.add_locatie'



class LocationListView(ListView):
    template_name = "location/list_of_locations.html"
    model = Location
    context_object_name = "all_locations"
    # permission_required = 'locatie.add_locatie'

class LocationUpdateView(UpdateView):
    template_name = 'location/update_location.html'
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('list_of_locations')



class LocationDeleteView(DeleteView):
    template_name = 'location/delete_location'
    model = Location
    success_url = reverse_lazy('list_of_locations')



class SportCreateView(CreateView):
    template_name = "sport/create_sport.html"
    model = Sport
    form_class = SportForm
    success_url = reverse_lazy("list_of_sports")  # unde se duce dupa ce dam submit
    # permission_required = 'sport.add_sport'


class SportListView(ListView):
    template_name = 'sport/list_of_sports.html'
    model = Sport
    context_object_name = "all_sports"


class SportUpdateView(UpdateView):
    template_name = 'sport/update_sport.html'
    model = Sport
    form_class = SportForm
    success_url = reverse_lazy('list_of_sports')



class SportDeleteView(DeleteView):
    template_name = 'sport/delete_sport.html'
    model = Sport
    success_url = reverse_lazy('list_of_sports')


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


