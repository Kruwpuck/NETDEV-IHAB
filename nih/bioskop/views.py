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
            request.session['movie_id'] = movie_id
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

def payment(request):
    selected_seats = request.session.get('selected_seats', [])
    movie_id = request.session.get('movie_id')
    movie = get_object_or_404(Movie, id=movie_id) if movie_id else None
    seat_price = 50000  # Harga per kursi
    total_price = len(selected_seats) * seat_price

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Lakukan logika penyimpanan data pembayaran di sini jika diperlukan
            request.session['total_price'] = total_price
            return redirect('payment_success')
    else:
        form = PaymentForm()

    return render(request, 'bioskop/payment.html', {
        'form': form,
        'selected_seats': selected_seats,
        'total_price': total_price,
        'movie': movie
    })

def payment_success(request):
    selected_seats = request.session.get('selected_seats', [])
    total_price = request.session.get('total_price')
    movie_id = request.session.get('movie_id')
    movie = get_object_or_404(Movie, id=movie_id) if movie_id else None

    # Memastikan data film diakses dari database dan ditampilkan di invoice
    if movie:
        movie_title = movie.title
        movie_showtime = movie.showtime
    else:
        movie_title = "Unknown"
        movie_showtime = "Unknown"

    return render(request, 'bioskop/payment_success.html', {
    'selected_seats': selected_seats,
    'total_price': total_price,
    'movie': movie
})


def about(request):
    return render(request, 'aboutUs.html')
