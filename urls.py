
from django.conf.urls import patterns, include, url
from comments.views import submit_comment

urlpatterns = patterns('',
    url(r'^submit/$', submit_comment, name="comments.submit"),
)
