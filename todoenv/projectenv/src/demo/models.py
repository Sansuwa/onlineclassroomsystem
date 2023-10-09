from django.db import models

# Create your models here.

class Status(models.TextChoices):
    DRAFT = "draft" , "DRAFT"
    PUBLISH = "publish" , "PUBLISH"
    BLOCKED = "blocked" , "BLOCKED"


class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(
        max_length=50,
        choices=Status.choices,
        default=Status.DRAFT
    )
    
    def __str__(self):
        return self.name

