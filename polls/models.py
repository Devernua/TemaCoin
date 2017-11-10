from django.db import models

class Image(models.Model):
	# author = models.ForeignKey(user)
	name = models.CharField(max_length=200)
	img = models.ImageField(upload_to='polls', blank=True, null=True)

	def __str__(self):
		return self.name

