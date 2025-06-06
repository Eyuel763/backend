from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        
        ordering = ['-created_at']

    def __str__(self):
        """
        String representation of the Task model.
        """
        return self.title