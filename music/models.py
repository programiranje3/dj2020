from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField, ForeignKey, DateField, BooleanField
from django.urls import reverse


class Band(models.Model):

    name = CharField(max_length=50, default='unknown')
    country = CharField(max_length=50, default='unknown')
    start = IntegerField(blank=True, null=True, verbose_name='The year when the band started performing together')
    end = IntegerField(blank=True, null=True, verbose_name='The year when the band stopped performing together')

    def __str__(self):
        name_str = f'{self.name} '
        country_str = f'({self.country}), '
        start_str = f'{self.start}-' if self.start else '...-'
        end_str = f'{self.end}' if self.end else '...'
        return name_str + country_str + start_str + end_str

    def get_absolute_url(self):
        return reverse('band-detail', args=[str(self.id)])


class Musician(models.Model):

    INSTRUMENT = [
        ('rhythm guitar', 'rhythm guitar'),
        ('lead guitar', 'lead guitar'),
        ('bass', 'bass'),
        ('drums', 'drums'),
        ('vocals', 'vocals'),
    ]

    ALIVE = [
        (True, 'alive'),
        (False, 'deceased'),
    ]

    name = CharField(max_length=50, default='unknown')
    band = ForeignKey(Band, on_delete=models.SET_NULL, null=True, blank=True)
    instrument = CharField(max_length=50, verbose_name='Primary instrument', default='rhythm guitar', choices=INSTRUMENT)
    born = DateField(null=True, blank=True)
    alive = BooleanField(null=True, blank=True, verbose_name='Alive/Deceased', choices=ALIVE)

    def __str__(self):
        name_str = f'{self.name} '
        band_str = f'({self.band.name}), ' if self.band else '(solo musician), '
        instrument_str = f'{self.instrument}; '
        born_str = f'born {self.born.isoformat()}; ' if self.born else 'birth date unknown; '
        alive_str = 'alive' if self.alive else 'deceased'
        return name_str + band_str + instrument_str + born_str + alive_str

    def get_absolute_url(self):
        return reverse('musician-detail', args=[str(self.id)])
