from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile, WishItem

from checkout.models import Order
from courses.models import Course


#@login_required
def profile(request):
    # Display the user's profile
    
    profile = get_object_or_404(UserProfile, user=request.user)
    
    orders = profile.orders.all()
    

    template = 'profiles/profile.html'
    context = {
        
        #'orders': orders,
        #'on_profile_page': True
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