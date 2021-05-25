from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.

"""
class Uzytkownik(models.Model):
    nazwa_uzytkownika = models.CharField('Nazwa Użytkownika', max_length=100)
    imie = models.CharField('Imię', max_length=100)
    nazwisko = models.CharField('Nazwisko', max_length=100)
    email = models.CharField('e-mail', max_length=100)
    haslo = models.CharField('Hasło', max_length=100)
    autoryzacja = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Użytkownik"
        verbose_name_plural = "Użytkownicy"

    def __unicode__(self):
        return self.nazwa_uzytkownika
"""


class Wiadomosci(models.Model):
    tytul = models.CharField('Tytuł', max_length=255)
    tresc = models.TextField(verbose_name='Treść')
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField('Data dodania', auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Obrazek: ")

    class Meta:
        verbose_name = "Wiadomość"
        verbose_name_plural = "Wiadomości"

    def __unicode__(self):
        return self.tytul