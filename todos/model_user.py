from django.db import models
from datetime import datetime

# Create your models here.

# User model
class users(models.Model):
  id = models.IntegerField(primary_key=True, null=False, blank=False)
  userId = models.CharField(max_length=100, null=False, blank=False) 
  password = models.CharField(max_length=20, null=False, blank=False)

def __str__(self):
  """Return a human readable representation of the model instance."""
  return "{}".format(self.name)