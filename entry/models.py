from django.db import models

class Entry(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(db_index=True, max_length=100)
    email = models.CharField(db_index=True, max_length=128)
    password = models.CharField(max_length=64)
    type = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    adult = models.IntegerField(default = 1)
    child = models.IntegerField(default = 0)
    picture = models.CharField(max_length=256, default=None)
    departure = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    time = models.DateTimeField(auto_now=True)

    def comments(self):
        return Comment.objects.filter(userid=self).all()

    def likes(self):
        return Like.objects.filter(userid=self).all()

class Comment(models.Model):
    resid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Entry, on_delete=models.CASCADE)
    commenter = models.IntegerField(default = 0)
    message = models.TextField(blank=True)
    time = models.DateTimeField(auto_now=True)

    def commenterinfo(self):
        return Entry.objects.filter(userid=self.commenter).first()

class Like(models.Model):
    likeid = models.AutoField(primary_key=True)
    userid = models.ForeignKey(Entry, on_delete=models.CASCADE)
    liker = models.IntegerField(default = 0)
    time = models.DateTimeField(auto_now=True)