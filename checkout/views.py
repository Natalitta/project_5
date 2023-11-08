from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
#from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
# from .models import Order, OrderItem
#from courses.models import Course
#from profiles.forms import UserProfileForm
#from profiles.models import UserProfile
#from bag.contexts import bag_contents

import stripe
import json


# Create your views here.
def checkout(request):
    # stripe_public_key = settings.STRIPE_PUBLIC_KEY
    # stripe_secret_key = settings.STRIPE_SECRET_KEY

    # if request.method == 'POST':
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty")
        return redirect(reverse('courses'))

    order_form = OrderForm(form_data)

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        # 'stripe_public_key': stripe_public_key,
        # 'client_secret': intent.client_secret,
    }

    return render(request, template, context)