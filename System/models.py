from django.db import models

class Category(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"