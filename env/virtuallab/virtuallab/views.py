from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate

def home_page(req):
    return render(req,"home.html",{})