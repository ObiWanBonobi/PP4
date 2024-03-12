""" Models for the blog page """

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class Socials(models.Model):
    """
    Connects to :model:`auth.User`, then connects to itself through the ManyToManyField
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )
    user_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        """ This method gives our posts a nicer title in the admin page """
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Connects to :model:`auth.User` and :model:`user_profile.Socials`.
    Follows own account when created.
    """
    if created:
        user_profile = Socials(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.socials)
        user_profile.save()
