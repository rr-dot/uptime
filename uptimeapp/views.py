from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Url
import requests
# Create your views here.

def index(req):
	template=loader.get_template('uptimeapp/index.html')
	for url in Url.objects.all():
		try:
			resp=requests.get(url.url)
			url.cur_status=resp.status_code
			url.exception_msg=''
		except Exception as e:
			url.exception_msg=str(e)
		url.save()
	context={'urls': Url.objects.all()}
	return HttpResponse(template.render(context,req))

def addurl(req):
	template=loader.get_template('uptimeapp/addurl.html')
	context={}
	if req.POST:
		u=req.POST['url'].strip()
		if len(u):
			url=Url(url=req.POST['url'],cur_status=-1,exception_msg='')
			url.save()
			return redirect('/')
	return HttpResponse(template.render(context,req))

