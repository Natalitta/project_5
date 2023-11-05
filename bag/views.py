from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from courses.models import Course

def view_bag(request):
    # To view the shopping bag page
    return render(request, 'bag/bag.html')

