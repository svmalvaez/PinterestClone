from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Picture(models.Model):
	name = models.CharField(max_length=30, null=True, blank=True)
	description = models.TextField(max_length=50, null=True, blank=True)
	photo = models.ImageField(upload_to='static/img/')
	like = models.BooleanField(default=False)
	user = models.ForeignKey(User)

class Tablero(models.Model):
	name = models.CharField(max_length=30, null=True, blank=True)
	picture = models.ForeignKey(Picture)
	user = models.ForeignKey(User)