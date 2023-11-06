from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
# from django.contrib import messages

from courses.models import Course


def view_bag(request):
    # To view the shopping bag page
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # To add a course to the bag
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    # Remove an item from the shopping bag

    course = get_object_or_404(Course, pk=item_id)
    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)