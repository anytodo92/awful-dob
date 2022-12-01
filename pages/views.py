from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import blogs,Index
from .forms import blogform,blogmodelform

# Create your views here.


def contact(request):
    return render(request, 'blogs/contact.html')


def index(request):
    index_data = Index.objects.all()
    #homepage_data = HomePage.objects.get(id=1)
    context = {
        'head':index_data[0].head,
        'para':index_data[0].para,
        'para2':index_data[0].para2,
        'skills':index_data[0].skills,
        'softwares':index_data[0].softwares,
        'mail':index_data[0].mail,
        'image':index_data[0].image,
    }
    return render(request, "pages/Index.html",context)



def blog(request):
    blogs_list = blogs.objects.all()

    context = {
        'blogs_list':blogs_list,
    }
    
    return render(request, "blogs/blog.html",context)



def blogdetail(request, id):
    blog=blogs.objects.get(id=id)
    context = {
                'blog': blog,
            }
    return render(request, 'blogs/blogdetail.html', context)

def blog_create(request):
    if request.method=='POST': 
        form=blogform(request.POST,request.FILES)
        if form.is_valid():
            blogs.objects.create(**form.cleaned_data)
            return redirect('/blogs')                 
        else:
            print("form is not valid")
            print(form.errors)
    else:
        form=blogform()
    return render(request,'blogs/create.html',{'form':form})
def blog_update(request,id):
    blog = blogs.objects.get(id=id)
    if request.method == 'POST':
        form = blogmodelform(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            #Blog.objects.filter(id=id).update(**form.cleaned_data)
            form.save()
            return redirect('/blogs')
        else:
            print('form is not valid')
            print(form.errors)
            return HttpResponse('error')
    else:
        form =  blogmodelform(instance=blog)
    return render(request, 'blogs/blog_update.html', {'form': form})  
def blog_delete(request,id):
    blog = blogs.objects.get(id=id)
    blog.delete()
    return redirect('/blogs')