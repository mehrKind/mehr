from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_view(request):

    if request.method == "POST":
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            #login
            login(request,user)
            return redirect("articles:list")
    else:
        forms = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':forms})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # LOGIN user
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("articles:list")