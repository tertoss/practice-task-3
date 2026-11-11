from django.db import models

class UserGreeting(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")

    def __str__(self):
        return self.name
