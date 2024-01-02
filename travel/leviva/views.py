from django.http import HttpResponse
from django.template import loader

def leviva(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('view.html')
  return HttpResponse(template.render())