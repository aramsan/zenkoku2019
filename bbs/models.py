# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime

class Thread(models.Model):
    #名前
    name = models.CharField(max_length=200, blank=False)
    #メアド
    email = models.CharField(max_length=200, blank=False)
    #お問い合わせの内容
    message = models.TextField(blank=False)
    #登録日時
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
      verbose_name = u'スレッド'

    def comments(self):
        return Comment.objects.filter(thread=self).all()

    def __unicode__(self):
        return self.message

class Comment(models.Model):
    #スレッド
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    #名前
    name = models.CharField(max_length=200, blank=False)
    #メアド
    email = models.CharField(max_length=200, blank=False)
    #回答
    message = models.CharField(max_length=200, blank=False)
    #登録日時
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u'コメント'

    def __unicode__(self):
        return self.message