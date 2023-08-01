from django.contrib.auth.models import User
from django.db import models

class blogs(models.Model):
    image=models.ImageField(upload_to='blog_images/')
    title=models.CharField(max_length=200)
    detail=models.TextField(max_length=500)
    post_date=models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(blogs, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.comment_text[:50]}"

