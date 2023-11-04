import random
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.utils.http import url_has_allowed_host_and_scheme # formerly is_safe_url

from .forms import TweetForm
from .models import Tweet
from .serializers import TweetSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.

def home_page(request):

    return render(request, 'pages/home.html', context = {} ,status = 200)

def tweet_create_view(request,*args,**kwargs):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    print('ajax', is_ajax)
    form = TweetForm(request.POST or None)
    # print('post data is', request.POST)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if is_ajax:
            return JsonResponse({},status=201) #201 is for created items
        if next_url != None and url_has_allowed_host_and_scheme(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/tweet_form.html', context={'form':form})


def tweet_list_view(request,*args,**kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """

    query_set=Tweet.objects.all()
    tweets_list=[{"id":x.id,"content":x.content, "likes":random.randint(0,12345)} for x in query_set]
    data={
        "isUser":False,
        "response":tweets_list
    }

    return JsonResponse(data)

def tweet_detail_view(request,tweet_id,*args,**kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """

    data = {
        "id":tweet_id,
    } 

    status=200

    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
        # serializer=TweetSerializers(obj,many=False)
        # return
    except:
        data['message']='Not found'
        status=404

    return JsonResponse(data,status=status)