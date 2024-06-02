from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Movie, Seat
from .forms import SignupForm, LoginForm

# Home page
def index(request):
    return render(request, 'index.html')

# Signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if username == 'dandy@gmail.com' and password == 'team1234':
                    login(request, user)
                    return redirect('/admin/')  # Redirect to Django admin
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Logout page
def user_logout(request):
    logout(request)
    return redirect('login')

# Seat selection page
@login_required(login_url='login')
def choose_seat(request, movie_id):
    # Fetch movie and seat details
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)
    
    if request.method == 'POST':
        selected_seats = request.POST.getlist('seat')
        request.session['selected_seats'] = selected_seats
        return redirect('payment')

    context = {
        'movie': movie,
        'seats': seats,
    }
    return render(request, 'choose_seat.html', context)
