from django.db import models

# Create your models here.
from django.db import models

PriorityEnum = {
  "HIGH" : 'HIGH',
  "MEDIUM" : 'MEDIUM',
  "LOW" : 'LOW',
}
class Task(models.Model):
    title = models.CharField(max_length=127)
    description = models.CharField(max_length=300, null=True, blank=True)
    priority = models.CharField(max_length=20, choices=list(PriorityEnum.items()))
    dueDate = models.DateField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f'{self.id} - {self.title}'

