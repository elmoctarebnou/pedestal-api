from django.db import models
from django.utils import timezone


class Sample(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, null=True)

    class meta:
        db_table = "sample_table"
