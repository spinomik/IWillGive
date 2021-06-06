from django.db import models

INSTITUTION_CHOICE = [
    ('F','fundacja'),
    ('OP','Organizacja pozarządowa'),
    ('ZL','Zbiórka lokalna')]
class Category(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

class Institution(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    description = models.TextField()
    type = models.CharField(max_length=2, choices=INSTITUTION_CHOICE, default='F')
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Instytucja"
        verbose_name_plural = "Instytucje"

