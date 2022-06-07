from django.contrib import admin

from teams import views
from django.urls import path

urlpatterns = [

    path("", views.HomeTemplateView.as_view(), name="home"),
    path('admin/', admin.site.urls),

    path('create-event/', views.EventCreateView.as_view(), name="create_event"),
    path('list-of-events/', views.EventListView.as_view(), name="list_of_events"),
    path('create-player/', views.PlayerCreateView.as_view(), name="create_player"),
    path('list-of-players/', views.PlayerListView.as_view(), name="list_of_players"),
    path('create-location/', views.LocationCreateView.as_view(), name="create_location"),
    path('list-of-locations/', views.LocationListView.as_view(), name='list_of_locations'),
    path('create-sport/', views.SportCreateView.as_view(), name="create_sport"),
    path('list_of_sports/', views.SportListView.as_view(), name="list_of_sports"),
    path('create-user/', views.UserExtendCreateView.as_view(), name='create_user'),

]