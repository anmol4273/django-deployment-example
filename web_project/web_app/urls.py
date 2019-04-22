from django.conf.urls import url,include
from web_app import views
app_name='web_app'
urlpatterns=[
url(r'^tom_jerry/$',views.tom_jerry,name='tom_jerry'),
url(r'^scooby/$',views.scooby,name='scooby'),
]
