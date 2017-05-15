
'''为登录应用user 定义的URL'''

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns=[
	#登录页面
	url(r'^login/$', login, {'template_name': 'user/login.html'}, name='login'),
	#定义一个用户注销的页面
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register, name='register'),
]
