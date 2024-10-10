from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import AdminLoginForm

def login_view(request):
    if request.method == "POST":
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
    else:
        form = AdminLoginForm()
    return render(request, 'admin_panel/login.html', {'form': form})

@login_required
def admin_dashboard(request):
    return render(request, 'admin_panel/dashboard.html')
