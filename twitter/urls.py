"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from twitterapp import views as appviews
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', appviews.homepage, name='home'),
	url(r'^globalfeed/$', appviews.globalfeed, name='globalfeed'),
	url(r'^user/(?P<username>\w{0,50})/$', appviews.userfeed, name='userfeed'),
	url(r'^userfollow/$', appviews.followpost, name='followpost'),
	url(r'^posttweet/$', appviews.posttweet, name='posttweet'),
	url(r'^retweet/$', appviews.retweet, name='retweet'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^signup/$',appviews.UserRegister.as_view()),
]
