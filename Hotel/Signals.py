from django.db.models.signals import post_save,post_delete
from django.dispatch import  receiver
from .models import  Room

@receiver(post_save,sender=Room)
def update_number_of_rooms(sender,instance,**kwargs):
    instance.hotel.NumberOfRooms=instance.hotel.rooms.count()
    instance.hotel.save()


@receiver(post_delete, sender=Room)
def update_number_of_rooms_on_delete(sender, instance, **kwargs):
    instance.hotel.NumberOfRooms = instance.hotel.rooms.count()
    instance.hotel.save()
