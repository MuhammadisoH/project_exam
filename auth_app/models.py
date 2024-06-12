from django.db import models


from django.db import models

class Kirim(models.Model):
    SUMMA_CHOICES = [
        ('naqt', 'Naqt pul'),
        ('karta', 'Karta'),
        ('valyuta', 'Valyuta')
    ]
    
    CHIQIM_TURI_CHOICES = [
        ('yolkira', "Yo'lkira"),
        ('tushlik', 'Tushlik'),
        ('salomatlik', 'Salomatlik')
    ]

    summa = models.DecimalField(max_digits=10, decimal_places=2)
    sana = models.DateField()
    hisoblar = models.CharField(max_length=50, choices=SUMMA_CHOICES)
    chiqim_turi = models.CharField(max_length=50, choices=CHIQIM_TURI_CHOICES)

    def __str__(self):
        return f"{self.summa} - {self.sana} - {self.hisoblar} - {self.chiqim_turi}"
