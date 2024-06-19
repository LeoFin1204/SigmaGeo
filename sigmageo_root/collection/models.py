from django.db import models

# Create your models here.
class UserTexList(models.Model):
  username = models.CharField(primary_key=True, max_length=120)
  tex_list = models.TextField(null=True)

  def __str__():
    return self.username


class Problem(models.Model):
  id = models.IntegerField(primary_key=True)
  num = models.CharField(max_length=5, default='')
  grade = models.CharField(max_length=5)
  text = models.TextField(null=False)
  solution = models.TextField(default='')
  themes = models.TextField(default='[]')
  source = models.CharField(max_length=250, default='')
  year = models.CharField(max_length = 20, null=True)
  stage = models.CharField(max_length=150, default='')
  author = models.CharField(max_length=150, default='')
  dif = models.IntegerField(choices={i : i for i in range(11)})


class Olimp(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=250, null=False)
  stages = models.TextField(default='[]')


class Book(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=250, null=False)
  chapters = models.TextField(default='[]')

class Theme(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=250, null=False)
  description = models.TextField(null=True)
  edu_tasks = models.TextField(default='[]')
