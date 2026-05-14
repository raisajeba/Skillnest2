from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from exchanges.models import ExchangeRequest
from .models import Rating
from .forms import RatingForm


@login_required
def submit_rating(request, exchange_id):
    exchange = get_object_or_404(
        ExchangeRequest,
        id=exchange_id,
        sender=request.user,
        status='accepted'
    )

    if hasattr(exchange, 'rating'):
        return redirect('exchange_home')

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.exchange = exchange
            rating.rater = request.user
            rating.rated_user = exchange.receiver
            rating.save()
            return redirect('exchange_home')
    else:
        form = RatingForm()

    return render(request, 'ratings/rate_form.html', {
        'form': form,
        'exchange': exchange
    })


@login_required
def user_ratings(request):
    ratings = Rating.objects.filter(rated_user=request.user).order_by('-created_at')
    return render(request, 'ratings/user_ratings.html', {'ratings': ratings})
