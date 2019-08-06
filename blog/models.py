from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    draft = models.TextField(null=False)
    published_date = models.DateField()
    author = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True, validators=[URLValidator()])

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')