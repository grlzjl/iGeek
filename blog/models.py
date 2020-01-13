from django.db import models

class UserInfo(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    user_pwd = models.CharField(max_length=20)

class BlogInfo(models.Model):
    date = models.DateField(blank=True, null=True)
    content = models.TextField(blank=False, null=False)
    number = models.FloatField(blank=True, null=True)
    type = models.TextField(blank=False, null=False)
    user = models.ForeignKey(UserInfo, to_field='user_name', on_delete=models.CASCADE)

