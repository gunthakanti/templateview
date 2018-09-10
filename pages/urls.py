from django.urls import path
from .views import Homepage, aboutpage
urlpatterns=[
	path('about/',aboutpage.as_view(),name='About'),
	path('',Homepage.as_view(),name='Home'),
]