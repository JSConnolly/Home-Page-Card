#!/usr/bin/env python
# encoding: utf-8
"""
views.py

Created by Ryan Walton on 2012-08-21.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

from django.shortcuts import render_to_response
from django.template.loader import get_template

def home_page(request):
    return render_to_response('home_page.html', )

def projects_page(request):
    return render_to_response('projects_page.html', )

def learning_page(request):
    return render_to_response('learning_page.html', )

