from django.db import models


# Model specjalizacji
class Types(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_detail_url(self):
        return f'{self.id}/'
    def sum_of_parts(self):
        return Workers.objects.filter(type=self).count()

# Model pracownika
class Workers(models.Model):
    name= models.CharField(max_length=100)
    type = models.ForeignKey(Types, on_delete=models.CASCADE)
    work = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name
    def get_detail_url(self):
        return f'{self.id}/edit_work/'
