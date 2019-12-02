from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.

class Blog(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    article = models.TextField()
    post_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.CharField(max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse('blog_detail', args=[str(self.id)])


class Comment(models.Model):

    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100, blank=True, editable=False)
    comment_text = models.TextField()
    comment_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.comment_text
  
    def get_absolute_url(self, **kwargs):
        return reverse('blog_detail', args=[str(self.blog_id)])

