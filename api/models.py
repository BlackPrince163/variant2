from django.db import models


class ToDoList(models.Model):
    to_do = models.CharField(max_length=200)
    done = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    until_date = models.DateField()

    def __str__(self):
        return self.to_do


