"""
Definition of urls for Edu4.
"""

from django.conf.urls import include, url
import Edu4Test.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', Edu4Test.views.index, name='index'),
    url(r'^home$', Edu4Test.views.index, name='home'),
]
