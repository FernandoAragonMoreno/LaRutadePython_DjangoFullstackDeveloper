from django.db import models

# Create your models here.
class UserProfile(models.Model):
  code = models.IntegerField()
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  name = models.CharField(max_length=255)
  profession = models.CharField(max_length=255)
  gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=255)
  city = models.CharField(max_length=255)

  def __str__(self):
    return f'Name: {self.name}, Profession: {self.profession}'
