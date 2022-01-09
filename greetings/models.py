from django.db import models
from datetime import datetime

class Greeting(models.Model):
    email = models.EmailField(max_length=40, primary_key=True)
    
    def __str__(self):
        return self.email