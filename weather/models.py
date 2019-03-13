from django.db import models
from django.conf import settings

# Create your models here.


class City(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          on_delete=models.PROTECT)
    city = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.city)[:50]

    class Meta:
        verbose_name = 'city name'
        verbose_name_plural = 'Cities'
