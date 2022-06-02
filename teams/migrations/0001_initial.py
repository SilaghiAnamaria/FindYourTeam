# Generated by Django 4.0.4 on 2022-05-31 17:56

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenume', models.CharField(max_length=20)),
                ('numar_minim_de_jucatori', models.IntegerField()),
                ('numar_maxim_de_jucatori', models.IntegerField()),
                ('descriere', models.TextField(max_length=1000)),
                ('gen', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('dificultate', models.CharField(choices=[('incepator', 'Incepator'), ('intermediar', 'Intermediar'), ('avanasat', 'Avansat')], max_length=20)),
                ('creat_in', models.DateTimeField(auto_now_add=True)),
                ('actualizat_in', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenume', models.CharField(max_length=60)),
                ('oras', models.CharField(max_length=20)),
                ('adresa', models.CharField(max_length=30)),
                ('descriere', models.TextField(max_length=1000)),
                ('deschis', models.BooleanField(default=True)),
                ('creat_in', models.DateTimeField(auto_now_add=True)),
                ('actualizat_in', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=20)),
                ('prenume', models.CharField(max_length=20)),
                ('porecla', models.CharField(max_length=20)),
                ('varsta', models.IntegerField()),
                ('oras', models.TextField(max_length=30)),
                ('descriere', models.TextField(max_length=1000)),
                ('gen', models.CharField(choices=[('barbat', 'Barbat'), ('femeie', 'Femeie')], max_length=10)),
                ('activ', models.BooleanField(default=True)),
                ('creat_in', models.DateTimeField(auto_now_add=True)),
                ('actualizat_in', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenume', models.CharField(max_length=60)),
                ('oras', models.CharField(max_length=30)),
                ('descriere', models.TextField(max_length=1000)),
                ('numar_minim_de_jucatori', models.IntegerField(verbose_name=2)),
                ('numar_maxim_de_jucatori', models.IntegerField(verbose_name=3)),
                ('creat_in', models.DateTimeField(auto_now_add=True)),
                ('actualizat_in', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserExtend',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('numar_telefon', models.CharField(max_length=15)),
                ('oras', models.CharField(max_length=15)),
                ('gen', models.CharField(choices=[('barbat', 'Barbat'), ('femeie', 'Femeie')], max_length=10)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
