from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def new(request):
  return HttpResponse("Hello, world. You're at the new page.")

