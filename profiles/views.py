from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, UserProfile, WishItem
from .forms import UserProfileForm

from checkout.models import Order
from courses.models import Course


#@login_required
def profile(request):
    # Display the user's profile
    
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please check the form filled in correctly')
    else:
        form = UserProfileForm(request.POST, instance=profile)
    
    orders = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


#@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_done.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    user = UserProfile.objects.get(user=request.user)
    wishlist_items = WishItem.objects.filter(user=user)
    return render(request, 'profiles/profile.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, course_id):
    course = Course.objects.get(id=course_id)
    user = UserProfile.objects.get(user=request.user)

    # Check if the course is already in the user's wishlist
    if not WishItem.objects.filter(user=user, course=course).exists():
        WishItem.objects.create(user=user, course=course)

    return redirect('course_detail', course_id=course_id)