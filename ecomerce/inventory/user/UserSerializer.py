from django.contrib.auth.models import User

# Import the Profile model from the models module

from ecomerce.inventory.user.Usermodel import Profile

# Import the serializers module from the rest_framework module
from rest_framework import serializers


# Create a ProfileSerializer class that inherits from serializers.ModelSerializer
class ProfileSerializer(serializers.ModelSerializer):
    # Specify the model and fields to use for serialization and deserialization
    class Meta:
        model = Profile
        fields = ["phone", "address"]


# Create a UserSerializer class that inherits from serializers.ModelSerializer
class UserSerializer(serializers.ModelSerializer):
    # Specify the model and fields to use for serialization and deserialization
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "profile",
        ]
        # Specify that password should be write-only and hashed when creating or updating a user object
        extra_kwargs = {"password": {"write_only": True}}

    # Override the create method to hash password when creating a user object
    def create(self, validated_data):
        # Pop the profile data from the validated data dictionary
        profile_data = validated_data.pop("profile")
        # Create a user object with the remaining validated data
        user = User.objects.create(**validated_data)
        # Set the password of the user object using the set_password method
        user.set_password(validated_data["password"])
        # Save the user object to the database
        user.save()
        # Create a profile object with the profile data and link it to the user object
        Profile.objects.create(user=user, **profile_data)
        # Return the user object
        return user

    # Override the update method to hash password when updating a user object
    def update(self, instance, validated_data):
        # Pop the profile data from the validated data dictionary
        profile_data = validated_data.pop("profile")
        # Get the profile object of the instance
        profile = instance.profile
        # Update the attributes of the instance with the remaining validated data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            # If password is updated, use the set_password method to hash it
            if attr == "password":
                instance.set_password(value)
        # Save the instance to the database
        instance.save()
        # Update the attributes of the profile object with the profile data
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        # Save the profile object to the database
        profile.save()
        # Return the instance
        return instance

    # Nest a ProfileSerializer inside the UserSerializer to serialize and deserialize related objects
    profile = ProfileSerializer()
