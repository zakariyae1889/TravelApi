from django.db import models
from django.utils.text import slugify

class Destination(models.Model):
    country=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to="destinations",blank=True,null=True)
    slug=models.SlugField(blank=True,null=True,allow_unicode=True)
    create=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.city,allow_unicode=True)
            return super(Destination,self).save(*args,**kwargs)
    def __str__(self):
        return f"{self.country} - {self.city}"
    
class Attraction(models.Model):
    destinations=models.ForeignKey(Destination,on_delete=models.CASCADE,related_name="attraction")
    name=models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="attractions", blank=True, null=True)
    openigHours=models.CharField(max_length=255,blank=True)
    ticketPrice=models.DecimalField(max_digits=6,decimal_places=2,null=True,blank=True,default=0.00)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name,allow_unicode=True)
            return super(Attraction,self).save(*args,**kwargs)
    def __str__(self):
        return f"{self.name}"