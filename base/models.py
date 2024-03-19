from django.db import models
# user model take cares of user information username,email,password
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    # one to many relationship (one user can have many items)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True) # user => model name, on_delete => what we need to perform when user get's deleted
    # models.CASCADE => delete all tasks when user get's deleted
    # models.SET_NULL => items will remain when user get's deleted
    # null=True => there could be empty field
    # blank = True => allows blank values

    # title will just a String
    title = models.CharField(max_length=200)

    #description will be TextField
    description = models.TextField(null=True, blank=True)

    #complete will be boolean 
    complete = models.BooleanField(default = False)

    #created will be datetimefeild
    # auto_now_add => automatically takes it when items creates
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']