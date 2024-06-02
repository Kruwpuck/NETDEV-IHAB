from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.http import HttpResponseRedirect

def handleLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')  # fix the password variable name
        
        # Authenticate the user
        user = authenticate(username=email, password=password)
        
        if user is not None:
            # Check if the user is active and not staff (non-admin)
            if user.is_active and not user.is_staff:
                # Login the user
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('/')
            else:
                messages.error(request, "Invalid credentials.")
        else:
            messages.error(request, "Invalid credentials.")
    return HttpResponseRedirect('/auth/login/')  # always redirect to login page

        
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')  # Ubah sesuai dengan atribut 'name'
        email = request.POST.get('email')  # Ubah sesuai dengan atribut 'name'
        password = request.POST.get('password')  # Ubah sesuai dengan atribut 'name'
        # ...


def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('/auth/login/')

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_url = f"/password/reset/{uid}/{token}/"
            messages.success(request, f"Password reset link has been sent to {email}.")
            return redirect(reset_url)
        except User.DoesNotExist:
            messages.error(request, "Email not registered.")
            return redirect('/')
    
    return render(request, 'password.html')
