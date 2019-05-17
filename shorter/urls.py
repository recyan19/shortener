from django.urls import path
from shorter import views

app_name = 'shorter'

urlpatterns = [
    path('', views.index, name='home'),
    path('shorten/', views.get_shorten_url, name='get-shorten'),
    path('my-urls/', views.user_urls, name='user-urls'),
    path('stats/', views.statistics, name='stats'),
    path('<str:url_id>/', views.get_original_url, name='get-origin'),
]