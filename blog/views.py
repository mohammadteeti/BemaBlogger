from django.shortcuts import render
from blog.forms import CommentForm
from blog.models import Post,Category,Comment
# Create your views here.

def blog_index(request):
    posts=Post.objects.all().order_by('-created_on')
    
    context={"posts":posts}
    for p in posts:
        print(p.pk)
    return render(request , "blog_index.html",context)


def blog_detail(request,pk):
    post=Post.objects.get(pk=pk)
    commentform =CommentForm() #empty form 
    
    if(request.method=='POST'):
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            c=Comment(author=commentform.cleaned_data["author"]
                        ,body=commentform.cleaned_data["body"]
                        ,post=post)
            c.save()
            
        
    comments = Comment.objects.filter(post=post)
    context ={"post":post,
              "comments":comments,
              "form":commentform} 
    
    return render(request,"blog_detail.html",context)


def blog_category(request,category):
    posts=Post.objects.filter(
        categories__name__contains=category).order_by(
            '-created_on'
        )
    
    context={
        "posts":posts,
        "category":category
    }
    
    return render(request,"blog_category.html",context)

