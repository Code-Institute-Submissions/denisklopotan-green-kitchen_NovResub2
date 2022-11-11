from django.db import models

# Create your models here.


class Contact(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.TextField(max_length=150)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"New message from {self.fname} {self.lname}: {self.body}"
