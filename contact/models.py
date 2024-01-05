from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    contact_email = models.EmailField()
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.contact_email
