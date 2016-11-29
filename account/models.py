from django.db import models
from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    descpition = models.CharField('个性签名', max_length=200, default='江湖第一美人')
    job = models.CharField('工作', max_length=200, default='美人')
    phone = models.CharField('手机', max_length=15, default='12345678910')
    photo = models.ImageField('头像图像', upload_to='user/%Y/%m/%d', blank=True)
    created = models.DateTimeField('创建时间', auto_now_add=True)
    updated = models.DateTimeField('发布时间', auto_now=True)
