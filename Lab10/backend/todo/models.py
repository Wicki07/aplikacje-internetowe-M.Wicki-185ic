from django.db import models


class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title
    assert errors[0].msg.startswith("CORS_ORIGIN_ALLOW_ALL should be") # to należy dodać
    
