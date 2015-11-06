from django.db import models

# Create your models here.

class Blog(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    url = models.URLField()
    votes = models.IntegerField(default=0)
