from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-created_at')[:5] # order by created_at desc limit 5
    template = loader.get_template('index.html')

    context = RequestContext(request, {
      'blog_list': blogs,
    })

    return HttpResponse(template.render(context))
