from django.db import models

# Create your models here.

class Book(models.Model):
  author = models.CharField(max_length=200)
  title = models.CharField(max_length=200)
  abbreviation = models.CharField(max_length=200, default='')
  image_filename = models.CharField(max_length=200)

  def __str__(self):
    return self.title

class User(models.Model):
  username = models.CharField(max_length=200)

  def __str__(self):
    return self.username

class Reflection(models.Model):
  contents = models.TextField()
  user = models.ForeignKey(User)

  def __str__(self):
    return self.contents

class Action(models.Model):
  contents = models.TextField()
  user = models.ForeignKey(User)

  def __str__(self):
    return self.contents

class Post(models.Model):
  contents = models.TextField()
  user = models.ForeignKey(User)

  def __str__(self):
    return self.contents
  
