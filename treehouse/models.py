from django.db import models

# Create your models here.

class Book(models.Model):
  author = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  image_filename = models.CharField(max_length=200)

class User(models.Model):
  username = models.CharField(max_length=200)

class Reflection(models.Model):
  contents = models.TextField()
  user = models.ForeignKey(User)

class Action(models.Model):
  contents = models.TextField()
  user = models.ForeignKey(User)

class Post(models.Model):
  contents = models.TextField()
  user = models.ForeignKey(User)
  
