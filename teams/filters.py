import django_filters
from django.forms import forms
from django_filters import DateTimeFilter, CharFilter
from teams.models import Event


class EventFilters(django_filters.FilterSet):
    de_la__gte = DateTimeFilter(field_name='start_date_time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), lookup_expr='gte', label='De la data de')
    pana_la__lte = DateTimeFilter(field_name='start_date_time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), lookup_expr='lte', label= 'Pana la data de')

    class Meta:
        model = Event
        fields = ['gender', 'first_name', 'last_name',  'start_date_time__gte', 'start_date_time__lte', 'end_date', 'activ']


    def __init__(self, *args, **kwargs):
        super(EventFilters, self).__init__(*args, **kwargs)
        self.filters['nume'].field.widget.attrs.update({'class': 'form-control', 'placeholder':'Please enter first name'})
        self.filters['oras'].field.widget.attrs.update({'class': 'form-control', 'placeholder':'Please enter last name'})
        self.filters['gen'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['de_la__gte'].field.widget.attrs.update({'class': 'form-control', })
        self.filters['pana_la__lte'].field.widget.attrs.update({'class': 'form-control', })
