from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Seat
from .forms import PaymentForm

def home(request):
    return render(request, 'home.html')

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
            request.session['movie_id'] = movie_id  # Store the movie_id in the session
            return redirect('payment')
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
    # Your payment logic here
    # You can use the movie_id parameter to fetch movie-specific data if needed
    return render(request, 'bioskop/payment.html', {'movie_id': movie_id})

def payment_success(request, movie_id):
    selected_seats = request.session.get('selected_seats', [])
    movie = get_object_or_404(Movie, id=movie_id) if movie_id else None

    if movie:
        movie_title = movie.title
        movie_showtime = movie.showtime
    else:
        movie_title = "Unknown"
        movie_showtime = "Unknown"

    # Calculate total price based on the number of selected seats
    total_price = len(selected_seats) * 50000

    return render(request, 'bioskop/payment_success.html', {
        'selected_seats': selected_seats,
        'total_price': total_price,
        'movie_title': movie_title,
        'movie_showtime': movie_showtime,
        'movie_id': movie_id,
    })



def about(request):
    return render(request, 'aboutUs.html')
