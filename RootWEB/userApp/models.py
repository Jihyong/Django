from django.db import models

# Create your models here.
# class - table : model에서 class를 만들고 table과 연결
# create table webuser(user_id varchar2(100))와 같은 작업
class WebUser(models.Model):
    user_id      = models.TextField(max_length=100)
    user_pwd     = models.TextField(max_length=100)
    user_name    = models.TextField(max_length=100)
    user_point   = models.IntegerField(default=1000)
    user_regdate = models.DateTimeField(auto_now=True)