from django.http import HttpResponse, Http404
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