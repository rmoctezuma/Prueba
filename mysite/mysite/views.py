from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime;

def hello(request):
	return HttpResponse("<!DOCTYPE html><html><head><title>django</title></head><body><h1>Hello world around.</h1></body></html>")

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404
	
	dt = datetime.datetime.now() + datetime.timedelta(hours = offset)
	html = "<html><body>En %s hora(s), seran las %s</body></html>" % (offset,dt)
	return HttpResponse(html)

def hello_user(request):
	return render_to_response('base.html',{'user': 'Raul', 'product': 'computer'})

def operadores(request):
	return render_to_response('Operadores.html', {'product' : 'El producto interno bruto', 'empresa' : 'timsa'})