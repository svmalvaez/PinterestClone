from django.db import models
from django.auth.contrib.models import User
# Create your models here.
class Picture(models.Model):
	name = models.CharField(max_length=30, null=True, blank=True)
	description = models.TextField(max_length=50 null=True, blank=True)
	photo = models.TextField(max_length=50 null=True, blank=True)
	like = models.BooleanField(default=False null=True, blank=True)
	user = models.ForeignKey(User)

class Tablero(models.Model):
	name = models.CharField(max_length=30 null=True, blank=True)
	picture = models.ForeignKey(Picture)
	user = models.ForeignKey(User)