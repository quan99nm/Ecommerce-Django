from django.contrib.auth.models import User
from django.db import models


# Create a Profile model that contains the additional fields
class Profile(models.Model):
    # Create a one-to-one link to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Create a phone field that stores the user's phone number
    phone = models.CharField(max_length=15)
    # Create an address field that stores the user's address
    address = models.TextField()

    # Define a string representation of the Profile model
    def __str__(self):
        return self.user.username
