from rest_framework import permissions
from rest_framework_jwt.utils import jwt_decode_handler
from django.shortcuts import redirect,render


class IsDaily(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        a = jwt_decode_handler(token[2])
        if a['role'] == 1:
            if request.method == 'POST':
                return True
            elif request.method == 'GET':
                return True
            else:
                return False
        elif a['role'] == 2 or a['role'] == 7:
            if request.method == 'POST':
                return False
            elif request.method == 'GET':
                return True
            else:
                return False
        else:
            print ("xsxs")
            return False


class IsHarry(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if trole['role'] == 2:
            return True
        else:
            if request.method == 'GET':
                return True
        return False

