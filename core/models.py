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


class Compartilhamento(models.Model):
    mes = models.IntegerField()
    ano = models.IntegerField()
    facebook = models.IntegerField(default=0)
    twitter = models.IntegerField(default=0)
    whatsapp = models.IntegerField(default=0)
    telegram = models.IntegerField(default=0)
    email = models.IntegerField(default=0)

    class Meta:
        ordering = ('mes', 'ano')
        unique_together = ['mes', 'ano']

    def __str__(self):
        return f'{str(self.mes)}-{str(self.ano)}'