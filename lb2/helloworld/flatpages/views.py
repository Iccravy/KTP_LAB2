#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
 return render(request, 'static_handler.html', {})
 #return HttpResponse(u"Привет, Мир!".encode('cp1251'), mimetype="text/plain")

