from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate


def home_page(req):
    template = "home.html"
    context = {
        "home": True,
        "simple": False,
        "double": False,
        "about": False
    }
    return render(req, template, context)


def about_page(req):
    template = "about.html"
    context = {
        "home": False,
        "simple": False,
        "double": False,
        "about": True
    }
    return render(req, template, context)
