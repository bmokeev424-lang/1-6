from django.db import models

class Equipment(models.Model):
    inv_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    status = models.CharField(max_length=20, default='working')

    def __str__(self):
        return self.inv_number


class MaintenanceRequest(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    description = models.TextField()
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заявка {self.id}"