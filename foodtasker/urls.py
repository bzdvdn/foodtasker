"""foodtasker URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from foodtaskerapp import views as foodtasker_app_views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings
from foodtaskerapp import apis as api


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', foodtasker_app_views.home, name='home'),

    #Restaurant
    url(r'^restaurant/sign-in/$', auth_views.login,
    	 {'template_name': 'restaurant/sign_in.html'
    	 },
    	 name='restaurant-sign-in'),
    url(r'^restaurant/sign-out/$', auth_views.logout,
    	{'next_page': '/'
    	},name='restaurant-sign-out'),
	 url(r'^restaurant/sign-up/$', foodtasker_app_views.restaurant_sign_up,
    	name='restaurant-sign-up'),   
    url(r'^restaurant/$', foodtasker_app_views.restaurant_home, name='restaurant-home'),
   
    url(r'^restaurant/accaunt/$', foodtasker_app_views.restaurant_accaunt, name='restaurant-accaunt'),
    url(r'^restaurant/meal/$', foodtasker_app_views.restaurant_meal, name='restaurant-meal'),
    url(r'^restaurant/meal/add/$', foodtasker_app_views.restaurant_add_meal, name='restaurant-add-meal'),
    url(r'^restaurant/meal/edit/(?P<meal_id>\d+)/$', foodtasker_app_views.restaurant_edit_meal, name='restaurant-edit-meal'),
    url(r'^restaurant/order/$', foodtasker_app_views.restaurant_order, name='restaurant-order'),
    url(r'^restaurant/report/$', foodtasker_app_views.restaurant_report, name='restaurant-report'),


    #Sign in/ Sign up/ /Sign out
    url(r'^api/social/', include('rest_framework_social_oauth2.urls')),
    # /convert-token(sign in/ sign up)
    # /revoke-token(sign out)

    url(r'api/restaurant/order/notification/(?P<last_request_time>.+)/$', api.restaurant_order_notification, name='restaurant_order_notification'),
    #api for customeres
    url(r'^api/customer/restaurants/$', api.customer_get_restaurant),
    url(r'^api/customer/meals/(?P<restaurant_id>\d+)/$', api.customer_get_meals),
    url(r'^api/customer/order/add/$', api.customer_add_order),
    url(r'^api/customer/order/latest/$', api.customer_get_latest_order),

    #api for drivers
    url(r'api/driver/orders/ready/$', api.driver_get_ready_orders, name="driver_get_ready_orders"),
    url(r'api/driver/order/pick/$', api.driver_pick_order),
    url(r'api/driver/order/latest/$', api.driver_get_latest_order),
    url(r'api/driver/order/complete/$', api.driver_complete_order),
    url(r'api/driver/revenue/$', api.driver_get_revenue),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
