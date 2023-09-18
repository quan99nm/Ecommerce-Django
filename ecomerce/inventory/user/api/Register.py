# Import the User model from Django's auth module
from django.contrib.auth.models import User

# Import the Profile model and serializer from the .models and .serializers modules
from ecomerce.inventory.user.Usermodel import Profile
from ecomerce.inventory.user.UserSerializer import UserSerializer

# Import the APIView class from the rest_framework.views module
from rest_framework.views import APIView

# Import the Response class from the rest_framework.response module
from rest_framework.response import Response

# Import the status module from the rest_framework module
from rest_framework import status


# Create a RegisterAPIView class that inherits from APIView
class RegisterAPIView(APIView):
    # Define a post method that takes a request as an argument
    def post(self, request):
        # Get the username, password, bio and location from the request data
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        # Validate the username and password
        if not username or not password:
            return Response(
                {"error": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if len(username) < 4 or len(password) < 6:
            return Response(
                {
                    "error": "Username must be at least 4 characters and password must be at least 8 characters"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already taken"}, status=status.HTTP_409_CONFLICT
            )

        # Create a user object with the username and password
        user = User.objects.create_user(
            username=username, password=password, email=email
        )

        # Create a profile object with the user, bio and location
        profile = Profile.objects.create(user=user)

        serializer = UserSerializer(user)

        # Return a 201 response with the serialized data
        return Response(serializer.data, status=status.HTTP_201_CREATED)
