from django.db import models
from datetime import datetime
from .model_user import users

# Create your models here.

# User model
#class users(models.Model):
 #       id = models.IntegerField(primary_key=True, null=False, blank=False)
  #      userId = models.CharField(max_length=100, null=False, blank=False) 
   #     password = models.CharField(max_length=20, null=False, blank=False)

#Todos model
class todo(models.Model):
        id = models.IntegerField(primary_key=True, null=False, blank=False)
        userId = models.ForeignKey(users, on_delete=models.CASCADE)
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_at = models.DateTimeField(default=datetime.now, blank=True, null=True)

def __str__(self):
  """Return a human readable representation of the model instance."""
  return "{}".format(self.name)