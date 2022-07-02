from datetime import datetime

from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse


# class EventAbstract(models.Model):
#     """ Event abstract model """
#
#     class Meta:
#         abstract = True
#
class EventManager(models.Manager):
    def get_query_set(self):
        now = datetime.now()
        return super(EventManager,self).get_query_set().filter(date__gte=now)

class Event(models.Model):

    gender_choices = (("Bărbaţi", "Bărbaţi"), ("Femei", "Femei"), ("Ambele", "Ambele"))
    dificulty_choices = (("Toate", "Toate"), ("Incepator", "Incepator"), ("Intermediar", "Intermediar"), ("Avansat", "Avansat"))
    city_choices = (("SIBIU", "SIBIU"), ("BRASOV", "BRASOV"), ("CLUJ-NAPOCA", "CLUJ-NAPOCA"))
    sport_type = (("Toate", "Toate"), ("Handbal", "Handbal"), ("Fotbal", "Fotbal"), ("Tenis de camp", "Tenis de camp"))

    nume = models.CharField(max_length=40)
    oras = models.CharField(max_length=30, choices=city_choices)
    gen = models.CharField(max_length=10, choices=gender_choices)
    de_la = models.DateTimeField(auto_now_add=True)
    pana_la = models.DateTimeField(auto_now_add=True)
    sporturi = models.CharField(max_length=15, choices=sport_type, default="")
    dificultate = models.CharField(max_length=20, choices=dificulty_choices)
    descriere = models.TextField(max_length=800)
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.gen} {self.dificultate}"


class Player(models.Model):
    gender_choices = (("man", "Bărbaţi"), ("women", "Femei"))

    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=20)
    porecla = models.CharField(max_length=20, null=True, blank=True)
    varsta = models.IntegerField()
    oras = models.TextField(max_length=30)
    descriere = models.TextField(max_length=1000, null=True,blank=True)
    gen = models.CharField(max_length=10, choices=gender_choices)
    poza = models.ImageField(upload_to='static/playerPicture/', null=True,blank=True)
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.prenume}"



class Location(models.Model):

    nume = models.CharField(max_length=100)
    oras = models.CharField(max_length=20)
    adresa = models.CharField(max_length=100)
    descriere = models.TextField(max_length=1000)
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.oras}"


class Sport(models.Model):
    gender_choices = (("man", "Bărbaţi"), ("women", "Femei"))

    nume = models.CharField(max_length=10)
    locatie = models.CharField(max_length=30, null=True, blank=True)
    oras = models.CharField(max_length=30)
    descriere = models.TextField(max_length=1000)
    numar_minim_de_jucatori = models.IntegerField()
    numar_maxim_de_jucatori = models.IntegerField()
    gen = models.CharField(max_length=10, choices=gender_choices, default="")
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.oras}"

class SportLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    description = models.CharField(max_length=264)

class PlayerSport(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    description = models.CharField(max_length=264)

class LocationEvent(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    description = models.CharField(max_length=264)

class UserExtendCreateView(User):
    gender_choices = (("man", "Bărbaţi"), ("women", "Femei"))

    nume = models.CharField(max_length=15)
    prenume = models.CharField(max_length=15)
    numar_telefon = models.CharField(max_length=15)
    oras = models.CharField(max_length=15)
    gen = models.CharField(max_length=10, choices=gender_choices)


    def __str__(self):
        return f"{self.nume} {self.prenume}"


class Photos(models.Model):
    nume = models.ImageField()

    # class EventAbstract(models.Model):
    #     """ Event abstract model """
    #
    #     class Meta:
    #         abstract = True
    #

    #class Event(models.Model):
    #""" Event model """

        #
        # title = models.CharField(max_length=200, unique=True)
        # description = models.TextField()
        # start_time = models.DateTimeField(null=True)
        # end_time = models.DateTimeField(null=True)
        #
        # def __str__(self):
        #     return self.title

        # def get_absolute_url(self):
        #     return reverse("calendarapp:event-detail", args=(self.id,))
        #
        # @property
        # def get_html_url(self):
        #     url = reverse("calendarapp:event-detail", args=(self.id,))
        #     return f'<a href="{url}"> {self.title} </a>'
