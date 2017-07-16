# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect, render


def home(request):
    return render(request, 'index.html')


def user_login(request):
    if request.user.is_authenticated():
        return core(request)
    else:
        return render(request, '')


def host_login(request):
    pass

def checkin(request):
    return render(request, 'checkin.html')


def wallets(request):
    return render(request, 'wallets.html')


def profile(request, ursername):
    page_user = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {})


def hackers_list(request):
    return render(request, 'people.html')


def projects(request):
    return render(request, 'projects.html')
