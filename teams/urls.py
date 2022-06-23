from django.contrib import admin

from teams import views
from django.urls import path

urlpatterns = [

    path("", views.HomeTemplateView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('login_user', views.login_user, name='login'),
    path('create-user/', views.UserExtendCreateView.as_view(), name='create_user'),
    path('create-event/', views.EventCreateView.as_view(), name="create_event"),
    path('list-of-events/', views.EventListView.as_view(), name="list_of_events"),
    path('create-player/', views.PlayerCreateView.as_view(), name="create_player"),
    path('list-of-players/', views.PlayerListView.as_view(), name="list_of_players"),
    path('create-location/', views.LocationCreateView.as_view(), name="create_location"),
    path('list-of-locations/', views.LocationListView.as_view(), name='list_of_locations'),
    path('create-sport/', views.SportCreateView.as_view(), name="create_sport"),
    path('list_of_sports/', views.SportListView.as_view(), name="list_of_sports"),
    path('update-sport/<int:pk>/', views.SportUpdateView.as_view(), name='update_sport'),
    path('update-event/<int:pk>/', views.EventUpdateView.as_view(), name='update_event'),
    path('update-location/<int:pk>/', views.LocationUpdateView.as_view(), name='update_location'),
    path('update-user/<int:pk>/', views.PlayerUpdateView.as_view(), name='update_player'),
    path('delete-sport/<int:pk>/', views.SportDeleteView.as_view(), name='delete_sport'),
    path('delete-event/<int:pk>/', views.EventDeleteView.as_view(), name='delete_event'),
    path('delete-location/<int:pk>/', views.LocationDeleteView.as_view(), name='delete_location'),
    path('delete-user/<int:pk>/', views.PlayerDeleteView.as_view(), name='delete_player'),
    path('list_of_photos/', views.PhotosListView.as_view(), name="list_of_photos"),
    path('image-upload/', views.PhotosListView.as_view(), name='image_upload')


]