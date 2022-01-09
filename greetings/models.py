from django.db import models
from datetime import datetime

class Greeting(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    
    def __str__(self):
        return self.name