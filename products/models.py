from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/img')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
        

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.slug)])
        
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)