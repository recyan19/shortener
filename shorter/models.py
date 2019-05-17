from django.db import models
from django.conf import settings


class Url(models.Model):
    url_id = models.SlugField(max_length=6, primary_key=True)
    url = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.url
