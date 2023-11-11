from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .models import UserProfile, WishItem
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

    form = UserProfileForm(instance=profile)
    
    orders = profile.orders.all()
    
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


class Wishlist(generic.View):
    def get(self, *arg, **kwarg):

        wish_items = WishItem.objects.filter(user=request.user)
        template = 'profiles/profile.html'
        context = {
            'wish_items': wish_items,
            #'on_profile_page': True
        }
        return render(request, template, context)