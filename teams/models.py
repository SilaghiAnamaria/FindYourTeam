from django.db import models

from django.contrib.auth.models import User



class Event(models.Model):
    gender_choices = (("male", "Male"), ("female", "Female"))
    dificulty_choices = (("incepator", "Incepator"), ("intermediar", "Intermediar"), ("avanasat", "Avansat"))
    city_choices = (("SIBIU", "SIBIU"), ("BRASOV", "BRASOV"), ("CLUJ-NAPOCA", "CLUJ-NAPOCA"))


    nume = models.CharField(max_length=20)
    oras = models.CharField(max_length=30, choices=city_choices)
    descriere = models.TextField(max_length=1000)
    gen = models.CharField(max_length=10, choices=gender_choices)
    numar_minim_de_jucatori = models.IntegerField()
    numar_maxim_de_jucatori = models.IntegerField()
    dificultate = models.CharField(max_length=20, choices=dificulty_choices)
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.gen} {self.dificultate}"




class Player(models.Model):
    gender_choices = (("barbat", "Barbat"), ("femeie", "Femeie"))

    nume = models.CharField(max_length=20)
    prenume = models.CharField(max_length=20)
    porecla = models.CharField(max_length=20)
    varsta = models.IntegerField()
    oras = models.TextField(max_length=30)
    descriere = models.TextField(max_length=1000)
    gen = models.CharField(max_length=10, choices=gender_choices)
    activ = models.BooleanField(default=True)
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.prenume}"


class Location(models.Model):

    nume = models.CharField(max_length=60)
    oras = models.CharField(max_length=20)
    adresa = models.CharField(max_length=30)
    descriere = models.TextField(max_length=1000)
    deschis = models.BooleanField(default=True)
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.oras}"


class Sport(models.Model):
    gender_choices = (("barbat", "Barbat"), ("femeie", "Femeie"))
    nume = models.CharField(max_length=60)
    oras = models.CharField(max_length=30, )
    locatie = models.ForeignKey(Location, on_delete=models.CASCADE)
    descriere = models.TextField(max_length=1000)
    numar_minim_de_jucatori = models.IntegerField()
    numar_maxim_de_jucatori = models.IntegerField()
    gen = models.CharField(max_length=10, choices=gender_choices)
    creat_in = models.DateTimeField(auto_now_add=True)
    actualizat_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume} {self.oras}"



class UserExtendCreateView(User):
    gender_choices = (("barbat", "Barbat"), ("femeie", "Femeie"))


    numar_telefon = models.CharField(max_length=15)
    oras = models.CharField(max_length=15)
    gen = models.CharField(max_length=10, choices=gender_choices)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
