from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from . models import Tweet
from . forms import TweetForm
# Create your views here.

def tweet_add(request):

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tweet_list')) 
        else:
            return HttpResponse('something is wrong, please check your data...')
    
    else:
        form = TweetForm() 


def tweet_list(request):

    tweet = Tweet.objects.all().order_by('-created_at') 
    return render(request, 'tweetList.html', {'tweet':tweet})


def like_tweet(request,tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    tweet.like_count += 1 
    tweet.save() 
    return HttpResponseRedirect(reverse('tweet_list'))


def delet_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id) 
    tweet.delete() 
    return HttpResponseRedirect(reverse('tweet_list'))
    

def edit_tweet(request, tweet_id):

    if request.method == 'GET':
        edit_tweet = Tweet.objects.get(id = tweet_id) 
        return render(request, 'tweetEdit.html', {'edit_tweet':edit_tweet}) 
    

    elif request.method == 'POST':
        edit_form = TweetForm(request.POST, request.FILES)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect('/') 
        
    
