from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from common.forms import UserForm

# Create your views here.

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # 사용자 인증
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render( request, 'common/signup.html', {'form': form})

def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render( request, 'common/404.html', {})