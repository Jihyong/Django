from django.db import models

# Create your models here.
class WebBbs(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    content = models.TextField()
    regdate = models.DateTimeField(auto_now=True)
    viewcnt = models.IntegerField(default=0)


class WebComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    txt = models.CharField(max_length=500)
    wtiter = models.CharField(max_length=100)
    bbs_id = models.ForeignKey(WebBbs, on_delete=models.CASCADE, db_column='bbs_id')