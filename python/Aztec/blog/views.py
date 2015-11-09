from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.order_by('-created_at')[:5] # order by created_at desc limit 5
    # template = loader.get_template('index.html')

    context = RequestContext(request, {
      'blog_list': blogs,
    })

    # return HttpResponse(template.render(context))
    return render(request, 'index.html', context) # shortcuts

def show(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'show.html', {'blog': blog})

# def show(request, id):
#     try:
#         blog = Blog.objects.get(id=id)
#     except Blog.DoesNotExist:
#         raise Http404("Blog does not exist")
#     return render(request, 'show.html', {'blog': blog})
