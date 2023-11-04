from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Course, Category


# Create your views here.
def all_courses(request):
    # A view to show all products, including sorting and search queries

    courses = Course.objects.all()

    context = {
        'courses': courses,

    }

    return render(request, 'courses/courses.html', context)


def course_detail(request, course_id):
    # A view to show individual product details

    course = get_object_or_404(Course, pk=course_id)

    context = {
        'courses': courses,
    }

    return render(request, 'course/course_detail.html', context)
