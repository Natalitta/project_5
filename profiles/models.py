from django.db import models
from django.contrib.auth.models import User
from courses.models import Course, Category
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    # A user profile model for order history and wish list

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=False, blank=False)
    default_email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    
    # To create or update the user profile
    
    if created:
        UserProfile.objects.create(user=instance)

    # Existing users: just save the profile
    instance.userprofile.save()


class WishItem(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    category = models.ForeignKey('courses.Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.course.name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'course')
