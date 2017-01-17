from django.views.generic.edit import CreateView
from twitterapp.models import Follow
from twitterapp.models import Tweet,Retweet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from itertools import chain
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

@login_required(login_url='login/')
def homepage(request):
	username = request.user.get_username()
	userid = int(request.user.id)
	userids = []
	userids.append(userid)
	follow = Follow.objects.filter(user_id=userid)
	for i in follow:
		userids.append(i.target_id)
	tweets = Tweet.objects.filter(user__in=userids).order_by('-created_at')
	retweets = Retweet.objects.filter(user__in=userids).order_by('-created_at')
	tweets = list(chain(tweets,retweets))
	tweets.sort(key=lambda item:item.created_at, reverse=True)
	return render(request, 'newsfeed.html', {'tweets': tweets,'username':username}) 

@login_required(login_url='login/')
def globalfeed(request):
	username = request.user.get_username()
	userid = int(request.user.id)
	userids = []
	userids.append(userid)
	follow = Follow.objects.filter(user_id=userid)
	for i in follow:
		userids.append(i.target_id)
	tweets = Tweet.objects.all()
	retweets = Retweet.objects.all()
	tweets = list(chain(tweets,retweets))
	tweets.sort(key=lambda item:item.created_at, reverse=True)
	return render(request, 'globalfeed.html', {'tweets': tweets,'username':username}) 


@login_required(login_url='login/')
def userfeed(request,username):
	userid = User.objects.get(username=username).pk
	tweets = Tweet.objects.filter(user=userid).order_by('-created_at')
	follow = Follow.objects.filter(user_id=request.user,target_id=userid)
	if follow:
		follow = 1
	else:
		follow = 0	
	return render(request, 'userfeed.html', {'tweets': tweets,'username':username,'follow':follow,'target_id':userid})

@csrf_exempt
@login_required(login_url='login/')
def followpost(request):
	
	if request.method == 'POST':
		target_id = int(request.POST['target_id'])
		userid = int(request.user.id)
		data = Follow.objects.filter(user_id=userid,target_id=target_id)
		if data:
			data[0].delete()
		else:
			Follow.objects.create(user_id=userid,target_id=target_id)	
		return HttpResponse("Done")

@csrf_exempt
@login_required(login_url='login/')
def posttweet(request):
	if request.method == 'POST':
		Tweet.objects.create(user_id=request.user.id,text=request.POST['text'])
		return HttpResponsePermanentRedirect("/")

@csrf_exempt
@login_required(login_url='login/')
def retweet(request):
	if request.method == 'POST':
		Retweet.objects.create(user_id=request.user.id,text=request.POST['text'],tweet_id=request.POST['tweet_id'])
		return HttpResponsePermanentRedirect("/")

class UserRegister(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        valid = super(UserRegister, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        
        login(self.request, new_user)
        return valid