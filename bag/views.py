from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from courses.models import Course


def view_bag(request):
    # To view the shopping bag page
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # To add a course to the bag
    course = get_object_or_404(Course, pk=item_id)
    quantity = 1
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(
            request, f'Added the course {course.name} to your bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_bag_item(request, item_id):
    # Remove an item from the shopping bag
    course = get_object_or_404(Course, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(
            request, f'Removed the course {course.name} from your bag'
            )

        request.session['bag'] = bag
        # return HttpResponse(status=200)
        return redirect(reverse('view_bag'))

    except Exception as e:
        return HttpResponse(status=500)
