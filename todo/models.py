from django.db import models

# Create your models here.

class Todo(models.Model):
    PRIORITY = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    )
    task = models.CharField(max_length=40)
    description = models.TextField(blank=True, max_length=100)
    priority = models.SmallIntegerField(choices=PRIORITY, default=3)
    is_completed = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    # Bu metod db'de nasıl görüneceğini sağlıyor başka işe yaramıyor
    def __str__(self):
        return f'{self.task}'