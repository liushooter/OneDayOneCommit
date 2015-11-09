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
        if form.is_valid():
            blog = form.save()
            return redirect('blog.views.show', id=blog.id)
        else:
            return HttpResponse(form.errors)
    else:
        form = BlogForm()
        render(request, 'index.html')

def edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = BlogForm(instance=blog)
    return render(request, 'edit.html', {'form': form, 'blog_id': blog.id })

def update(request, id):
    if request.POST:
        blog = get_object_or_404(Blog, id=id)
        form = BlogForm(request.POST, instance=blog)

        if form.is_valid():
            form.save()
            return redirect('blog.views.show', id=blog.id)
        else:
            return HttpResponse(form.errors)
    else:
        return render(request, 'index.html')

def destroy(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()

    return redirect('blog.views.index')

# def show(request, id):
#     try:
#         blog = Blog.objects.get(id=id)
#     except Blog.DoesNotExist:
#         raise Http404("Blog does not exist")
#     return render(request, 'show.html', {'blog': blog})
