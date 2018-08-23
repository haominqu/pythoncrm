from django.db import models
from userinfo.models import *
# Create your models here.

DAIORNY = (
        (1, 'daily'),
        (2, 'harryny'),

    )


class ToEmail(models.Model):
    daiorny = models.IntegerField(choices=DAIORNY,default=1)
    user = models.ForeignKey(UserInfo,verbose_name='项目经理',related_name='managera')
    touser = models.ForeignKey(UserInfo,verbose_name='收件人',related_name='recivea')