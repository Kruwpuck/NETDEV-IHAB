from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie, Seat, Image
from .forms import PaymentForm

#from django.contrib import messages
#from bioskop.models import Contact,Blogs,Internship
# Create your views here.
def home(request):
    return render(request,'home.html')
'''
def movie_list(request):
    movies = Movie.objects.all()
    pics = Image.objects.all()
    return render(request, 'bioskop/movie_list.html', {"movies": movies}, {"pics":pics})
'''
def movie_list(request):
    movies = Movie.objects.all()  # Asumsi Anda memiliki model Movie
    return render(request, 'bioskop/movie_list.html', {'movies': movies})

def choose_seat(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == 'POST':
        selected_seats = request.POST.getlist('seat')
        if selected_seats:
            request.session['selected_seats'] = selected_seats
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
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            return redirect('payment_success')
    else:
        form = PaymentForm()
    return render(request, 'bioskop/payment.html', {'form': form, 'selected_seats': selected_seats})

def payment_success(request):
    return render(request, 'bioskop/payment_success.html')

