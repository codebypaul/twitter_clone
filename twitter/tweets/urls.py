from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page, name = 'home page'),
    path('tweets',views.tweet_list_view, name = 'tweet list view'),
    path('tweet/<int:tweet_id>',views.tweet_detail_view, name = 'specific tweet view'),
]