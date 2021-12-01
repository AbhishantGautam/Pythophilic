from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.
class Topics(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    details = models.CharField(max_length=300)
    rating = models.IntegerField()
    slug = models.SlugField(default="", null=False, db_index=True)


    def save(self,*args,**kwargs): 
        self.slug = slugify(self.title) 
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.title