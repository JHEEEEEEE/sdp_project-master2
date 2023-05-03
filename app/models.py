from django.db import models

# 회원 정보
class User(models.Model):
  email = models.CharField(max_length=20 )
  name = models.CharField(max_length=20)
  pwd = models.CharField(max_length=20)
  c_date = models.DateTimeField()

  def __str__(self):
    return self.name