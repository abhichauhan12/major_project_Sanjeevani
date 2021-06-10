from django.db import models
from PIL import Image

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    item_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(default = 'default.jpg', upload_to = 'thumbnails')
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)
    received_quantity = models.IntegerField(default=0, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    Schedule_H = models.BooleanField(default=0)

    def __str__(self):
        return self.item_name
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})