## Overview

Simple comments that can be attached to any content type. The comments start in NEW state and require manual approval for comments to get displayed on the site.

This is a fork of [django-comments](https://github.com/kylefox/django-comments). The comments app appears to be a lightweight alternative to built Django comments that are scheduled to be removed from the core distribution.

The original project is based on [django-simple-comments](http://code.google.com/p/django-simple-comments/) app. The original project has no documentation, but because it appears to be an almost exact copy of django-simple-comments one can take a look at django-simple-comments documentation.

## Installation

The installation instructions assume that you are working from within virtualenv environment on Python 2.7.

### Download code from github

Local site-packages is the best place to download the app to. Go to

	cd lib/python2.7/site-packages/
	git clone https://github.com/kylefox/django-comments.git

This creates django-comments directory. Rename it to be just comments:

	mv django-comments comments

### Configuration

#### settings.py

Add import statement if you already don't have one:

	from django.conf import global_settings

Add comments to your INSTALLED_APPS variable:

	INSTALLED_APPS = (
		'django.contrib.flatpages',
		...
		'comments',
	)

In the sample above flatpages is just part of the sample and is not required. The instructions will use flatpages as an example application to add comments to.

Add comments to TEMPLATE_CONTEXT_PROCESSORS. Make sure you don't override Django defaults. If you don't have TEMPLATE_CONTEXT_PROCESSORS variable defined, then you can simply add the following sample:

	TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
	    'comments.context_processors.user_info',
	)

At this point you can run syncdb command to create required database table:

	python manage.py syncdb

#### urls.py

Add the following line to your urlpatterns:

	url(r'^comments/', include('comments.urls')),


Example:

	urlpatterns = patterns('',
		url(r'^admin/', include(admin.site.urls)),
		url(r'^comments/', include('comments.urls')),
	)

## Usage

Comments introduce 2 custom django template tags. The example uses flatpages app to demonstrate how to add comments to your templates.

	{{ flatpage.content }}
	{% load comment_tags %}
	{% get_approved_comments for flatpage as comments %}
	{% if comments %}
	  <h2>Comments</h2>
	  {% for comment in comments %}
	  <h3>{{ comment.name }}</h3>
	  <p>{{ comment.comments }}</p>
	  {% endfor %}
	{% endif %}
	<h2>Leave Feadback</h2>
	{% comment_form flatpage %}

The example above demonstrates how to load custom tags wit line

	{% load comment_tags %}

Load approved comments for current flatpage object into the template context:

	{% get_approved_comments for flatpage as comments %}

Create comment form for flatpage object:

	{% comment_form flatpage %}

## Change Log

This is not a detailed log. It is simply a record of major adjustments.

### February 25, 2014

Updated core functionality to Django 1.6.

The app is known to run on Python 2.7.