from django.db import models

# Create your models here.
class Anime(models.Model):
    title=models.CharField(max_length=60)
    desc=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return f"Anime {self.title} | {self.desc}"

class Fans(models.Model):
    first_name=models.CharField(max_length=35)
    last_name=models.CharField(max_length=40)
    liked_anime=models.ManyToManyField(Anime, related_name="the_fans")
    notes=models.TextField(null=True)
    def __repr__(self):
        return f"Fans {self.first_name} {self.last_name}"
