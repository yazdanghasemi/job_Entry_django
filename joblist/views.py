from django.shortcuts import render,redirect
from .models import Employer
from django.urls import reverse
from django.contrib import messages
from .forms import EmployerForm
# Create your views here.


def job_list(request):
    jobs_lists = Employer.objects.all()
    if request.method == 'GET':
        form = EmployerForm()
        return render(request, 'joblist/job-list.html', {"jobs_lists": jobs_lists, "form": form})
    elif request.method == 'POST':
        form = EmployerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO,
                                 f"Your request was send successfuly !")
            return redirect(reverse('job-list'))
        else:
            messages.add_message(request,messages.ERROR,f"Your request was not send !")
            return render(request, "joblist/job-list.html", {"posts": jobs_lists, "form": form})