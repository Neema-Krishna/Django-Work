from django.contrib import admin
from .models import Post,Author,Tag,Comments

# Register your models here.

class Postadmin(admin.ModelAdmin):
    list_filter=('author','tags','date')
    list_display=('title','date','author')
    prepopulated_fields={'slug':('title',)}

class Commentadmin(admin.ModelAdmin):
    list_display=('user_name',"post")

admin.site.register(Post,Postadmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comments,Commentadmin)



 

