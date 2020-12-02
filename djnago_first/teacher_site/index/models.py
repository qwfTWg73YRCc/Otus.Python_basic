from django.db import models

# Create your models here.


class BaseModel(models.Model):
    id = models.PositiveIntegerField(primary_key= True, unique=True)

