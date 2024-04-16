from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django_resized import ResizedImageField

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Course(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    is_open = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video_url = models.URLField(max_length=1024, null=True, blank=True)
    video = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    image = ResizedImageField(
        null=True, blank=True,
        size=[300, 300], quality=75,
        upload_to='images/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]
        )
    posted_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["posted_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"