from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat
from .forms import PaymentForm

def home(request):
    return render(request, 'base.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bioskop/movie_list.html', {'movies': movies})

def choose_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seat')
        if selected_seats:
            request.session['selected_seats'] = selected_seats
            return redirect('payment', movie_id=movie_id)
        else:
            return render(request, 'bioskop/choose_seat.html', {
                'movie': movie,
                'seats': seats,
                'error_message': "Please select at least one seat."
            })

    return render(request, 'bioskop/choose_seat.html', {
        'movie': movie,
        'seats': seats
    })

def payment(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            return redirect('payment_success', movie_id=movie_id)
    else:
        form = PaymentForm()

    return render(request, 'bioskop/payment.html', {'form': form, 'movie_id': movie_id})

def payment_success(request, movie_id):
    selected_seats = request.session.get('selected_seats', [])
    movie = get_object_or_404(Movie, id=movie_id)
    movie_title = movie.title
    movie_showtime = movie.showtime
    total_price = len(selected_seats) * 50000

    # Mark the selected seats as booked
    Seat.objects.filter(id__in=selected_seats).update(booked=True)

    return render(request, 'bioskop/payment_success.html', {
        'selected_seats': selected_seats,
        'total_price': total_price,
        'movie_title': movie_title,
        'movie_showtime': movie_showtime,
        'movie_id': movie_id,
    })

def about(request):
    return render(request, 'aboutUs.html')
