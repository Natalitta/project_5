from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course

def bag_contents(request):

    bag_items = []
    total = 0
    course_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            course = get_object_or_404(Course, pk=item_id)
            total += item_data * course.price
            course_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'course': course,
            })

    # to open an MC if total is 100 or more
    if total >= settings.FREE_MC_THRESHOLD:
        gift_course = True

    context = {
        'bag_items': bag_items,
        'total': total,
        'course_count': course_count,
        'free_mc_threshold': settings.FREE_MC_THRESHOLD,
    }

    return context