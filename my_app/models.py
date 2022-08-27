from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="task")
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    # id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.name
        
    class Meta():
        ordering = ['-complete']