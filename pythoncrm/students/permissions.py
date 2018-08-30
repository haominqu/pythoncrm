from rest_framework import permissions
from rest_framework_jwt.utils import jwt_decode_handler
from django.shortcuts import redirect,render


class StudentLimit(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):

        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if trole['role'] == 25:
            return True
        elif request.method == 'GET':
            return True
        return  False

class MasterPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if trole['role'] == 5:
            return True
        else:
            return False
        return False