from django.db import models

class student(models.Model):

	first_name = models.TextField()
	last_name = models.TextField()