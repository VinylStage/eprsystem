from django.db import models

# Create your models here.
# model


class Product(models.Model):
    class Meta:
        db_table = 'products'

    code = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)

    # 생성될 때 stock quantity를 0으로 초기화 로직
