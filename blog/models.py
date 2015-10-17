from django.db import models

# Create your models here.



class Vprasanje(models.Model):
	text = models.TextField()

	def __str__(self):
		return self.text



class Odgovor (models.Model):
	vprasanje = models.ForeignKey(Vprasanje, related_name='odgovori')
	text = models.CharField(max_length=50)

	naslednje_vprasanje = models.ForeignKey(Vprasanje, related_name='prejsnja_vprasanja')