#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:25:00 2019

@author: sambhav
"""
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest.app.user.serializers import UserRegistrationSerializer
from rest.app.profile.models import UserProfile
import requests
import json


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                "success": "true",
                "status code": status_code,
                "message": "User profile fetched successfully",
                "data": [
                    {
                        "first_name": user_profile.first_name,
                        "last_name": user_profile.last_name,
                        "phone_number": user_profile.phone_number,
                        "age": user_profile.age,
                        "gender": user_profile.gender,
                    }
                ],
            }

            def get_client_ip(request):
                x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
                if x_forwarded_for:
                    ip = x_forwarded_for.split(",")[0]
                else:
                    ip = request.META.get("REMOTE_ADDR")
                return ip

            payload = {"user": user_profile.id, "ip": get_client_ip(request)}
            r = request.post(
                "https://encrusxqoan0b.x.pipedream.net/", data=json.dumps(payload)
            )
            print(r.text)
        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "success": "false",
                "status code": status.HTTP_400_BAD_REQUEST,
                "message": "User does not exists",
                "error": str(e),
            }
        return Response(response, status=status_code)
