from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

def signup(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')
        
        if get_password != get_confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('/auth/signup/')
        
        if User.objects.filter(username=get_email).exists():
            messages.warning(request, "Email is already taken.")
            return redirect('/auth/signup/')
        
        myuser = User.objects.create_user(username=get_email, email=get_email, password=get_password)
        myuser.save()

        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "User created and logged in successfully.")
            return redirect('/')
        else:
            messages.error(request, "User authentication failed. Please try again.")
            return redirect('/auth/login/')
    
    return render(request, 'signup.html')

def handleLogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')  # Mengambil nilai dari bidang 'password'
        
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
                return redirect('/auth/login/')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('/auth/login/')
    return render(request, 'login.html')


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
