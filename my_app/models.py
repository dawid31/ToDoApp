from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return self.name
