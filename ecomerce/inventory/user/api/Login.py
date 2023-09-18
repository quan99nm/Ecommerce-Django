# Import the User model from Django's auth module
from django.contrib.auth.models import User

# Import the Token model from the rest_framework.authtoken module
from rest_framework.authtoken.models import Token

# Import the APIView class from the rest_framework.views module
from rest_framework.views import APIView

# Import the Response class from the rest_framework.response module
from rest_framework.response import Response

# Import the status module from the rest_framework module
from rest_framework import status

from ecomerce.inventory.user.UserSerializer import UserSerializer


# Create a LoginAPIView class that inherits from APIView
class LoginAPIView(APIView):
    # Define a post method that takes a request as an argument
    def post(self, request):
        # Get the username and password from the request data
        username = request.data.get("username")
        password = request.data.get("password")

        # Try to find a user object that matches the username
        try:
            user = User.objects.get(username=username)
        # If no user is found, return a 404 response with an error message
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        # Check if the password of the user object is correct
        if user.check_password(password):
            # If yes, get or create a token for the user object
            token, created = Token.objects.get_or_create(user=user)
            # Return a 200 response with the token as data
            return Response(
                {"token": token.key, "info": UserSerializer(user).data},
                status=status.HTTP_200_OK,
            )
        # If no, return a 401 response with an error message
        else:
            return Response(
                {"error": "Wrong password"}, status=status.HTTP_401_UNAUTHORIZED
            )
