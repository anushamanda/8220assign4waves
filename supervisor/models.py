from django.db import models


class Supervisor(models.Model):
    name=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role=models.CharField(max_length=50)

    def __str__(self):
        return self.name
