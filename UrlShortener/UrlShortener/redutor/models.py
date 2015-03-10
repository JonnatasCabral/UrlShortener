from django.db import models
from django.conf import settings

class Link(models.Model):

	url_original = models.URLField('original' , max_length=200)
	url_generated = models.CharField(blank=True , max_length= 100)
	
	
	def __str__(self):
		return self.url_original

	