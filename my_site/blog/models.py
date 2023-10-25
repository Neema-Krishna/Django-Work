from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()
    
    

class Post(models.Model):

    title=models.CharField(max_length=50)
    excerpt=models.CharField( max_length=200)
    # image_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images',null=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(db_index=True,unique=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name='posts')
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Comments(models.Model):
    user_name=models.CharField(max_length=120)
    email=models.EmailField() 
    text=models.TextField(max_length=300)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name
    

