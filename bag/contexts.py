from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course

def bag_contents(request):

    bag_items = []
    total = 0
    course_count = 0
    free_mc = False
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        course = get_object_or_404(Course, pk=item_id)
        total += quantity * course.price
        course_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'course': course,
        })

    # to calculate delta to pay to get a free MC if total is 99 or more
    if total < settings.FREE_MC_THRESHOLD:
        free_mc_delta = settings.FREE_MC_THRESHOLD - total
    else:
        free_mc = get_object_or_404(Course, pk=1)
        free_mc.price = 0
        free_mc_delta = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'course_count': course_count,
        'free_mc_threshold': settings.FREE_MC_THRESHOLD,
        'free_mc_delta': free_mc_delta,
        'free_mc': free_mc,
    }

    return context