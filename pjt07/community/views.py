from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg, Prefetch

from .models import Review, Comment
from .forms import ReviewForm, CommentForm

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
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'community/form.html', context)

@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'community/detail.html', context)

@require_POST
def comments_create(request, review_pk):
    if request.user.is_authenticated:
    # review = get_object_or_404(Review, pk=review_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review_id = review_pk
            comment.user = request.user
            comment.save()
        return redirect('community:detail', review_pk)
    else:
        return redirect('accounts:login')
        

def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('community:detail', review_pk)

