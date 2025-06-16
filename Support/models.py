from django.db import models

# Create your models here.
class Support(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Support request from {self.name}"
