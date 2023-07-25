from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.


#There is two types of views one is function views and another one is class views
#It(views) will handle the traffic routes from home
# class based views handles the backend logic
#class based views are: create views, delete views, detial views, update views, list views... 
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model= Post
    template_name ='blog/home.html' 
    context_object_name= 'posts'
    ordering = ['-date_posted']
#postlistview -> It looks for <app>..<model>_<viewstype>.html

class PostDetailView(DetailView):
    model= Post


def about(request):
    return render(request, 'blog/about.html',{'title':'About Page'})