from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _ # i18n

# Create your views here.

def hello(request):
  output = _("hello world")
  return HttpResponse(output)
