from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import *
from django.contrib.auth.decorators import *
from .models import Review
from .forms import ReviewForm

# Create your views here.
@require_safe
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'community/index.html', context)

@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('community:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'community/form.html', context)

@require_safe
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    context = {
        'review' : review,
    }
    return render(request, 'community/detail.html', context)

@login_required
@require_http_methods(['GET','POST'])
def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', pk)

    else:
        form = ReviewForm(instance=review)
    context = {
        'form' : form,
    }
    return render(request, 'community/form.html', context)

@require_POST
@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('community:index')
    else:
        return redirect('community:detail', review.pk)