from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
import json

from shorter.models import Url
# from shorter.forms import UrlShortenerForm
from shorter.utils import get_short_code_for_url


def index(request):
    # form = UrlShortenerForm
    c = {}
    c.update(csrf(request))
    return render(request, 'shorter/index.html', c)


def get_original_url(request, url_id):
    url = get_object_or_404(Url, pk=url_id)
    url.count += 1
    url.save()

    if any(url.url.startswith(prt) for prt in ['https', 'http']):
        return HttpResponseRedirect(url.url)
    else:
        if url.url.startswith('www.'):
            return HttpResponseRedirect('http://' + url.url.strip('www.'))
        return HttpResponseRedirect('http://' + url.url)


def get_shorten_url(request):
    url = request.POST.get('url', '')

    if url != '':
        url_id = get_short_code_for_url()
        b = Url(url_id=url_id, url=url, created_by=request.user)
        b.save()

        response_data = dict()
        response_data['url'] = settings.SITE_URL + url_id
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")


def user_urls(request):
    if request.user.is_authenticated:
        urls = Url.objects.filter(created_by=request.user)
        site_url = settings.SITE_URL
        return render(request, 'shorter/user_urls.html', {'urls': urls, 'site_url': site_url})
    return redirect('/')


def statistics(request):
    if request.user.is_authenticated:
        urls = Url.objects.filter(created_by=request.user)
        site_url = settings.SITE_URL
        return render(request, 'shorter/user_urls_stats.html', {'urls': urls, 'site_url': site_url})
    return redirect('/')