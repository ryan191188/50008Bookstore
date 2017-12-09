"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
"""from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from mysite import views as core_views
#from myapp import views as book_views


urlpatterns = [
		#books
               url(r'^books/(?:[0-9]{3}-)?[0-9]{10}$', core_views.books, name = 'books' ),             
		 #logged in
               url(r'^accounts/login/',
                   auth_views.login,
                   {
                   'template_name': 'login.html'
                   },
                   name='login'
                   ),

	       
               url(r'^accounts/logout/',
                   auth_views.logout,
                   {
                   'template_name': 'logout.html'
                   },
                   name='logout'),

               url(r'^loginSuccess/',
                   core_views.loginSuccess, name='loginSuccess'),
               

	    #    url(r'^accounts/order/',
		   # core_views.orders,
     #               name='order'),
	       
               url(r'^admin/', admin.site.urls),

               #url(r'^bookstore/', include('myapp.urls')),
               
               url(r'^accounts/signup/',
                   core_views.signup, 
		                name='signup'),

               url(r'^search/',
                   core_views.search, 
		   name='search'),
		#user info
	       url(r'^user/.+/profile',
		   core_views.userdata,
		   name = 'user'),

		   url(r'^user/.+/feedback',
		   core_views.userfeedback,
		   name = 'userfeedback'),

		   url(r'^user/.+/ratings',
		   core_views.userratings,
		   name = 'userratings'),

       url(r'^user/.+/orders',
       core_views.userorders,
       name = 'userorders'),

		   url(r'^newbook',
		   core_views.newbook,
		   name = 'newbook'), 

		   url(r'^arrivebook',
		   core_views.arrivebook,
		   name = 'arrivebook'),

       url(r'^statistics',
       core_views.statistics,
       name = 'statistics')      
               ]
