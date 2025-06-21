from django.db import models

class Task(models.Model):
    task=models.CharField(max_length=300)
    is_completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
