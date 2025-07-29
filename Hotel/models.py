from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from destinations.models import Destination


class Hotel(models.Model):
     destination=models.ForeignKey(Destination,on_delete=models.CASCADE,related_name="hotels")
     name=models.CharField(max_length=255)
     location=models.CharField(max_length=255)
     phone=models.CharField(max_length=255,blank=True,null=True)
     rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

     description=models.TextField(blank=True)
     image=models.ImageField(upload_to="hotel",blank=True,null=True)
     slug=models.SlugField(blank=True,null=True,allow_unicode=True)
     create = models.DateTimeField(auto_now_add=True)
     update = models.DateTimeField(auto_now=True)

     @property #decoretor
     def numbr_of_rooms(self):
         return  self.rooms.count()

     def save(self, *args, **kwargs):
         if not self.slug:
                self.slug = slugify( self.name,allow_unicode=True)
         return super(Hotel, self).save(*args, **kwargs)

     def __str__(self):
         return f"{self.name}"

class Room(models.Model):
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,related_name="rooms")
    room_type=models.CharField(max_length=255)
    room_number=models.PositiveIntegerField(default=0)
    price=models.DecimalField(max_digits=6,decimal_places=2,default=0.00)
    is_available=models.BooleanField(default=True)
    image = models.ImageField(upload_to="hotel", blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    def clean(self):
       if Room.objects.filter(hotel=self.hotel,room_number=self.room_number,is_available=self.is_available).exclude(pk=self.pk).exists():
                raise ValidationError("this room alredy exists")

    def __str__(self):
        return f"{self.hotel.name}"
