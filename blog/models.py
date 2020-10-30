from django.db import models
from django.utils import timezone


class GonderiModel(models.Model):
    yazar = models.ForeignKey("auth.User",on_delete=models.CASCADE)
    baslik = models.CharField(max_length=200,verbose_name="Başlık")
    yazi = models.TextField(verbose_name="Blog Metni")
    olus_zaman = models.DateTimeField(default=timezone.now,verbose_name="Oluşturma Zamanı")
    yayim_zaman = models.DateTimeField(blank=True,null=True,verbose_name="Yayımlanma Zamanı")

    def yayimla(self):
        self.yayim_zaman = timezone.now()
        self.save()


    def __str__(self):
        return self.baslik + " " + str(self.olus_zaman)
