from django.db import models



class MaterialTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    material_one = models.IntegerField()

class TestAnalytics(models.Model):
    id = models.AutoField(primary_key=True)
    jan = models.IntegerField()
    feb = models.IntegerField()
    mar = models.IntegerField()
    apr = models.IntegerField()
    may = models.IntegerField()
    jun = models.IntegerField()
    jul = models.IntegerField()
    aug = models.IntegerField()
    sep = models.IntegerField()
    oct = models.IntegerField()
    nov = models.IntegerField()
    dec = models.IntegerField()
    