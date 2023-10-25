from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify

from django.urls import reverse

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=2)

    def __str__(self):
        return self.name
    

class Address(models.Model):
    street=models.CharField(max_length=50)
    postalcode=models.CharField(max_length=5)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postalcode}, {self.city}"
    
    class Meta:
        verbose_name_plural= 'Address Entities'

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()
    

class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name='books')
    is_bestselling=models.BooleanField(default=False)
    slug=models.SlugField(default="",blank=True,editable=False,null=False,db_index=True)
    published_countries=models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("details", args=[self.slug])
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(*args,**kwargs)
    

    def __str__(self):
        return self.title
    

