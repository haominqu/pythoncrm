from rest_framework import permissions
from rest_framework_jwt.utils import jwt_decode_handler
from django.shortcuts import redirect,render


class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):

        # Read permissions are allowed to any request
        if request.method == 'GET':
            token = request.META.get("HTTP_AUTHORIZATION").split(' ')
            a = jwt_decode_handler(token[2])
            if a['role']==1:
                return True
            else:
                print ("xsxs")
                return False
        return True


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


class ChManager(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):

        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if trole['role'] == 7:
            return True
        else:
            if request.method == 'GET':
                return True
        return False


class IsCenter(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if trole['role'] == 2:
            return True
        else:
            if request.method == 'GET':
                return True
        return False

class IsClassActive(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if trole['role'] == 7:
            return True
        else:
            return False
        return False

class IsClasses(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if trole['role'] == 2:
                return True
            else:
                return False
        else:
            return True
        return False

class EduPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        token = request.META.get("HTTP_AUTHORIZATION").split(' ')
        trole = jwt_decode_handler(token[2])
        if trole['role'] == 2:
            return True
        else:
            return False
        return False
