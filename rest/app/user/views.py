"""
Created on Thu Dec  6 14:04:16 2019

@author: sambhav
"""
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Custom serializer class built atop django abstract generic classes:
from rest.app.user.serializers import UserRegistrationSerializer
from rest.app.user.serializers import UserLoginSerializer


class UserRegistrationView(CreateAPIView):
    # serializer helps to retrieve data and parse it into json and vice versa
    # It also checks for exceptions: Validates whether data from POST request can be injected into the DB
    # It checks which fields are required in the models.py and sends an exception message accordingly
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    # Function for incoming POST requests: To inject the new user data into our DB
    # OR return exception message in JSON format if some data is inappropriate or missing
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # validates if it doesnt violate model/schema rules
        # Uses serializers.py for validation
        serializer.is_valid(raise_exception=True)
        # Adding the user into our DB
        serializer.save()
        # Stub response to let frontend know that the registration was successful
        response = {
            "success": "True",
            "status code": status.HTTP_200_OK,
            "message": "User registered  successfully",
        }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):
    # Allows users without JWT auth to request for registration:
    permission_classes = (AllowAny,)
    # the extended serializer that we coded earlier:
    serializer_class = UserLoginSerializer

    def post(self, request):
        # Passes request data to crete a form object serializer. here, 'serializer':
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Sending success response along with JWT token if valid:
        response = {
            "success": "True",
            "status code": status.HTTP_200_OK,
            "message": "User logged in  successfully",
            "token": serializer.data["token"],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)
