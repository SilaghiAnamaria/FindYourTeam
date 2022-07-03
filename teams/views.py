import form as form
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from teams.forms import EventForm, LocationForm, PlayerForm, SportForm
from teams.models import Event, Player, Location, Sport, UploadImage


class HomeTemplateView(TemplateView):
    template_name = "home/home.html"



class EventCreateView(CreateView):
    template_name = "event/create_event.html"
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("list_of_events")
    permission_required = 'event.add_event'


class EventListView(ListView):
    template_name = "event/list_of_events.html"
    model = Event
    context_object_name = "all_events"



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
    permission_required = 'user.add_player'


class PlayerListView(ListView):
    template_name = "player/list_of_players.html"
    model = Player
    context_object_name = "all_players"
    permission_required = 'user.add_player'

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
    permission_required = 'location.add_location'



class LocationListView(ListView):
    template_name = "location/list_of_locations.html"
    model = Location
    context_object_name = "all_locations"
    permission_required = 'location.add_location'

class LocationUpdateView(UpdateView):
    template_name = 'location/update_location.html'
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('list_of_locations')



class LocationDeleteView(DeleteView):
    template_name = 'location/delete_location.html'
    model = Location
    success_url = reverse_lazy('list_of_locations')



class SportCreateView(CreateView):
    template_name = "sport/create_sport.html"
    model = Sport
    form_class = SportForm
    success_url = reverse_lazy("list_of_sports")  # unde se duce dupa ce dam submit
    permission_required = 'sport.add_sport'


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
    success_url = reverse_lazy('login')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    else:
        return render(request, 'registration/login.html')


class PhotosListView(ListView):
    template_name = 'photos_list/list_of_photos.html'
    model = UploadImage
    context_object_name = "all_photos"


def player_image_view(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PlayerForm()
    return render(request, 'player/image_upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')

