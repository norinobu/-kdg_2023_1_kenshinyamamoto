from django.db import models
from django.urls import reverse

class Syoukai(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

class Article(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    content = models.TextField()
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.content
 
    def get_absolute_url(self):
        return reverse('bbs:detail', kwargs={'pk': self.pk})
 
class Comment(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    target = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
    )
    content = models.TextField('コメント')
    created_at = models.DateTimeField(auto_now_add=True)

 # Create your models here.
