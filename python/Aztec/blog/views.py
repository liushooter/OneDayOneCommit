from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from .models import Blog
from .forms import BlogForm

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

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form': form})

def create(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if True: #form.is_valid():
            blog = form.save()
            # blog.save()
            return redirect('blog.views.show', id=blog.id)
        else:
            return HttpResponse("is_valid")

    else:
        form = BlogForm()
        render(request, 'index.html')


# def show(request, id):
#     try:
#         blog = Blog.objects.get(id=id)
#     except Blog.DoesNotExist:
#         raise Http404("Blog does not exist")
#     return render(request, 'show.html', {'blog': blog})
