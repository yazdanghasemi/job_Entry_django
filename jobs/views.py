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
        return render(request, 'jobs/job.html', {"jobs_view": jobs_objects, "form": form})

    elif request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES)
        job_create_at = request.POST["job_create_at"]
        job_type_job = request.POST["job_create_at"]
        job_country = request.POST["job_create_at"]
        job_topic = request.POST["job_create_at"]
        job_income = request.POST["job_create_at"]
        job_logo = request.POST["job_create_at"]
        job_summary1 = request.POST["job_summary1"]
        job_summary2 = request.POST["job_summary2"]
        job_summary3 = request.POST["job_summary3"]
        job_summary4 = request.POST["job_summary4"]
        job_summary5 = request.POST["job_summary5"]
        job_response1 = request.POST["job_response1"]
        job_response2 = request.POST["job_response2"]
        job_response3 = request.POST["job_response3"]
        job_response4 = request.POST["job_response4"]
        job_response5 = request.POST["job_response5"]
        job_company1 = request.POST["job_company1"]
        job_company2 = request.POST["job_company2"]
        job_company3 = request.POST["job_company3"]
        job_company4 = request.POST["job_company4"]
        job_company5 = request.POST["job_company5"]
        detail = Employer.objects.create(
            create_at=job_create_at, type_job=job_type_job, country=job_country, income=job_income, topic=job_topic, logo=job_logo,
              summary1=job_summary1, summary2=job_summary2, summary3=job_summary3, summary4=job_summary4, summary5=job_summary5,
                response1=job_response1, response2=job_response2, response3=job_response3, response4=job_response4, response5=job_response5,
                  company1=job_company1,company2=job_company2,company3=job_company3,company4=job_company4,company5=job_company5)
        detail.save()
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
