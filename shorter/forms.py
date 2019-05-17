from django.forms import ModelForm

from shorter.models import Url


class UrlShortenerForm(ModelForm):
    class Meta:
        model = Url
        fields = ['url']
