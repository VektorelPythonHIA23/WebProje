from django.db import models
from django.utils import timezone

class IletisimModel(models.Model):
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=70)
    mesaj = models.TextField()
    zaman = models.DateTimeField(default=timezone.now)



    def __str__(self):
        liste = [self.adi,self.soyadi,str(self.zaman)]
        return '-'.join(liste)
