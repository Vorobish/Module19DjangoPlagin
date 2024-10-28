from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# python manage.py makemigrations
# python manage.py migrate
# Author.objects.create(name='Name 1', bio='Bio 1')
# python manage.py createsuperuser
