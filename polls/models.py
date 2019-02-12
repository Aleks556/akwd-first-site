import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Order(models.Model):
    SERVICE_TYPES = (
        ('1', 'Usluga 1'),
        ('2', 'Usluga 2'),
        ('3', 'Usluga 3'),
    )
    SIZES = (
        ('1', 'Maly'),
        ('2', 'Sredni'),
        ('3', 'Duzy'),
    )
    CUSTOMERS = (
        ('1', 'Klient nr 1'),
        ('2', 'Klient nr 2'),
        ('3', 'Klient nr 3'),
    )
    ZAMZAP = (
        ('1', "ZAMOWIENIE"),
        ('2', "ZAP"),
    )
    COPY_IDS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    order_id = models.IntegerField("Numer zamówienia", max_length=None)
    customer_fullname = models.CharField("Imię i nazwisko", max_length=60)
    services = models.CharField("Wyrób / Usługa", max_length=1, choices=SERVICE_TYPES)
    drawing_id = models.IntegerField("Numer rysunku", max_length=None)
    size = models.CharField("Rozmiar", max_length=1, choices=SIZES)
    customer = models.CharField("Klient", max_length=5, choices=CUSTOMERS)
    receiver = models.CharField("Odbiorca", max_length=5, choices=CUSTOMERS)
    price = models.IntegerField("Cena", max_length=None)
    term_date = models.DateTimeField("Termin")
    add_date = models.DateTimeField("Data")
    order_code = models.IntegerField("BARCOD", max_length=None)
    zamzap = models.CharField("ZAM / ZAP", max_length=1, choices=ZAMZAP)
    copy_id = models.CharField("Numer kopii", max_length=5, choices=COPY_IDS)
    def __str__(self):
        return self.customer_fullname
