from django.db import models

# Create your models here.

class AttestModel(models.Model):
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    tell = models.PositiveIntegerField()

    #vaqtlarni yozib olish
    ruyxatdanUtishVaqti = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "attestatsiya"