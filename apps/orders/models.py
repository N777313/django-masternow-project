from django.db import models


class Order(models.Model):

    class Status(models.TextChoices):
        NEW = 'new', 'New'
        CANCEL = 'cancel', 'Cancel'
        COMPLETED = 'completed', 'Completed'
        PENDING = 'pending', 'Pending'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)

    request_desc = models.TextField(max_length=4000)
    comment = models.TextField(max_length=2000, blank=True, null=True)

    # 📅 дата создания — автоматически текущая дата
    date_creation = models.DateTimeField(auto_now_add=True)

    # 📌 статус по умолчанию = NEW
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"
