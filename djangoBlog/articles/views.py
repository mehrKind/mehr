from django.shortcuts import redirect, render
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    articles = models.Articles.objects.all().order_by('-date')

    args = {'articles': articles}
    return render(request, 'articles/articleslist.html', args)

def articles_details(request,slug):
    # return HttpResponse(slug)
    article = models.Articles.objects.all().get(slug=slug)
    return render(request,"articles/articlesDetails.html",{'article':article})

@login_required(login_url="accounts:login")
def create_views(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            # save Articles
            # get ueser from request and = to Login user
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()

    return render(request,'articles/create_article.html',{'form':form})