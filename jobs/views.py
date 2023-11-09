from django.shortcuts import render, redirect
from django.urls import reverse
from joblist.models import Employer
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages
# Create your views here.


def index(request):

    if request.method == 'GET':
        return render(request, 'jobs/index.html', {})
    elif request.method == 'POST':
        return render(request, 'jobs/testimonial.html', {})


def job_detail(request, id):
    jobs_objects = Employer.objects.get(id=id)

    if request.method == 'GET':
        forms = EmployeeForm(request.POST, request.FILES)
        return render(request, 'jobs/job.html', {"jobs_view": jobs_objects, "forms": forms})

    elif request.method == 'POST':
        forms = EmployeeForm(request.POST, request.FILES)

        if forms.is_valid():
            forms.save()
            messages.add_message(request, messages.INFO,
                                 f"Your job request sent successfuly !")
            return redirect(reverse("job-detail", kwargs={"id": id}))
        else:
            messages.add_message(request, messages.ERROR,
                                 f"Your job request was not send !")
            return render(request, "jobs/job.html", {"jobs_view": jobs_objects, "forms": forms})


def category(request):
    if request.method == 'GET':
        return render(request, 'jobs/category.html', {})
    elif request.method == 'POST':
        pass


def error_404(request):
    if request.method == 'GET':
        return render(request, 'jobs/404.html', {})
    elif request.method == 'POST':
        pass


def about(request):
    if request.method == 'GET':
        return render(request, 'jobs/about.html', {})
    elif request.method == 'POST':
        pass


def contact(request):
    if request.method == 'GET':
        return render(request, 'jobs/contact.html', {})
    elif request.method == 'POST':
        pass


def test_page(request):
    jobs_request = Employee.objects.all()
    return render(request, 'jobs/testimonial.html', {"req": jobs_request})
