from django.db import models


class Silaba(models.Model):
    silaba = models.CharField(max_length=3)
    palavra1 = models.CharField(max_length=10, blank=True, null=True)
    palavra2 = models.CharField(max_length=10, blank=True, null=True)
    imagem1 = models.ImageField(upload_to='silabas', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='silabas', blank=True, null=True)

    class Meta:
        ordering = ('silaba',)

    def __str__(self):
        return self.silaba