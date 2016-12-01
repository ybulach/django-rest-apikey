import binascii
from django.contrib.auth.models import User
from django.db import models
import os

class APIKey(models.Model):
	key = models.CharField(max_length=40, primary_key=True)
	user = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.key:
			self.key = binascii.hexlify(os.urandom(20)).decode()
		return super(APIKey, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.key
