from django.shortcuts import render, redirect
from django.urls import reverse
from joblist.models import Employer
from joblist.forms import EmployerForm
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
        form = EmployerForm()
        return render(request, 'jobs/job-detail.html', {"jobs_view": jobs_objects, "form": form})

    elif request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES)
        job_create_at = request.POST["job_create_at"]
        job_type_job = request.POST["job_create_at"]
        job_country = request.POST["job_create_at"]
        job_topic = request.POST["job_create_at"]
        job_income = request.POST["job_create_at"]
        job_logo = request.POST["job_create_at"]
        job_summary_Employer = request.POST["job_create_at"]
        job_responsibility = request.POST["job_create_at"]
        job_company = request.POST["job_create_at"]
        summary = Employer.objects.create(
            create_at=job_create_at,type_job=job_type_job,country=job_country,income=job_income,topic=job_topic,logo=job_logo,summary_Employer=job_summary_Employer,responsibility=job_responsibility,company=job_company)
        summary.save()
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 f"Your job request sent successfuly !")
            return redirect(reverse("post-detail", kwargs={"id": id}))
        else:
            messages.add_message(request, messages.ERROR,
                                 f"Your job request was not send !")
            return redirect(reverse("post-detail"))



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


def test_page(request):
    if request.method == 'GET':
        return render(request, 'jobs/testimonial.html', {})
    elif request.method == 'POST':
        pass
