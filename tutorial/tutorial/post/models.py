from django.db import models

class Post(models.Model):
    name = models.CharField('投稿者',max_length='100')
    naiyou = models.TextField('投稿内容',max_length='250')


    def __str__(self):
        return self.name
