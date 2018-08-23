from celery import task
from .views import *
from userinfo.models import *
from daily.cexecl import *
import time
from daily.cexecl import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse,request
from daily.models import *
#  python3 me.py celery -A pythoncrm worker -B

@task
def auto_create_week_excel():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    response = CreateExcel(request,41)

    return True
@task
def aa():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    return True
@task
def send_daily(daily):
    # try:
    #     daily = Daily.objects.filter(id=id)
    # except ObjectDoesNotExist as e:
    #     logging(e)

    response = send_email(request, daily, 'quhm@tedu.cn')
    print("send success")
    pass