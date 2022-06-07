from django.db import models


# Create your models here.
class Filescsv(models.Model):
    id = models.AutoField(primary_key=True)
    roid = models.CharField(max_length=255, verbose_name='roid')
    domain_name = models.CharField(max_length=255, verbose_name='domain-name')
  #  creation_date = models.DateTimeField()

    class Meta:
        verbose_name = "Arquivo CSV"
        verbose_name_plural = "Arquivos CVS"
