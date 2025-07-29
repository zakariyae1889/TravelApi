from django.core.validators import MinValueValidator,MaxValueValidator

from destinations.models import  Destination


from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Restaurants(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="restuarant")
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cuisine_type = models.CharField(max_length=255)
    opening_hours = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.ImageField(upload_to="restaurant", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    @property
    def number_of_tables(self):
        return self.tables.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class tables(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name="tables")
    table_type = models.CharField(max_length=255)
    table_number = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)



    def clean(self):
        if tables.objects.filter(
            restaurant=self.restaurant,
            table_type=self.table_type,
            table_number=self.table_number
        ).exclude(pk=self.pk).exists():
            raise ValidationError("This table already exists in this restaurant.")

    def __str__(self):
        return f'{self.restaurant.name} - Table {self.table_number}'

