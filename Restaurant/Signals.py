from django.db.models.signals import post_save,post_delete
from django.dispatch import  receiver
from .models import tables

@receiver(post_save,sender=tables)
def update_number_of_table(sender,instance,**kwargs):
    instance.restaurant.NumberOfTable=instance.restaurant.tables.count()
    instance.restaurant.save()

@receiver(post_delete,sender=tables)
def delete_number_of_table(sender,instance,**kwargs):
    instance.restaurant.NumberOfTable=instance.restaurant.tables.count()
    instance.restaurant.save()
