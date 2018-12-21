from django.db import models
from django.conf import settings
from django.urls import reverse

from rest_framework.reverse import reverse as api_reverse
# Create your models here.
class BlogPost(models.Model):
    """This class represents a blog model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """A representation of the blog instance"""
        return str(self.user)

    @property
    def owner(self):
        """Returns the user who posted the blog"""
        return self.user

    def get_api_url(self, request=None):
        """Returns the url of a specific blog"""
        return api_reverse("api-postings:post-rud",
                           kwargs={'pk': self.pk}, request=request)
