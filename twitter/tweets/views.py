import random
from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet
from .serializers import TweetSerializer

# Create your views here.

def home_page(request):

    return render(request, 'pages/home.html', context = {} ,status = 200)


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