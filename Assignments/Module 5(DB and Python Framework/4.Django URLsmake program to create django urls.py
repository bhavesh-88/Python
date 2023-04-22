#What is Django URLs?make program to create django urls

"""
Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL,
matching against path_info . Once one of the URL patterns matches,
Django imports and calls the given view, which is a Python function (or a class-based view).
"""

from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path ('logout/',views.logout,name='logout'),
]
