from django.db import models
from categories.models import Category
from author.models import Author
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # ekta post multiple categorir moddhe thakte pare abar ekta categorir moddhe multiple post thakte pare
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title 
    


Author (One-to-Many with Posts): An author can have multiple blog posts.
Category (Many-to-Many with Posts): A blog post can belong to multiple categories.
Profile (One-to-One with User): Each user has a single profile.
    
    