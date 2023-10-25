from django.db import models

# Create your models here.

class Review(models.Model):
    user_name=models.CharField(max_length=100)
    review_text=models.TextField()
    rating=models.IntegerField()
    slug=models.SlugField(unique=True,db_index=True,null=True)
