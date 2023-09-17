from django.db import models


class Task(models.Model):
    task_detail = models.TextField(max_length=50)
    is_complete = models.BooleanField(default=False)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.task_detail
