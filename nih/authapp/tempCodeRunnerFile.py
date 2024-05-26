from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your views here.
def signup(request):
    
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')
        if get_password!=get_confirm_password:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup/')
        
        try:
            if User.objects.get(username=get_email):
                messages.warning(request,"Email is Taken")
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(get_email,get_email,get_password)
        myuser.save()

        myuser= authenticate(username=get_email,password=get_password)

        if myuser is not None:

            login(request,myuser)
            messages.success(request,"User Created & Login Success")
            return redirect('/')

        
    return render(request,'signup.html')

def handleLogin(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        myuser= authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'logout success')
    return render(request,'login.html')


def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Generate token
            token = default_token_generator.make_token(user)
            # Encode user ID
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            # Construct reset password URL
            reset_url = f"/password/reset/{uid}/{token}/"
            # Redirect to reset password page
            messages.success(request, f"Link reset password telah dikirim ke {email}.")
            return redirect(reset_url)
        except User.DoesNotExist:
            messages.error(request, "Email tidak terdaftar.")
            return redirect('/')
    
    return render(request, 'password.html')