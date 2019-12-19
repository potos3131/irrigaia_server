from django.db import models

# Create your models here.


class WeatherRules(models.Model):
    id_rule = models.IntegerField(primary_key=True)
    url_scrape=models.CharField(max_length=512)
    max_temp_param = models.CharField(max_length=32)
    min_temp_param = models.CharField(max_length=32)
