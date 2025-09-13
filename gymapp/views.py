# create views
from django.shortcuts import render, redirect
from .forms import MemberForm
from .models import Member

# Homepage
def home(request):
    return render(request, "gymapp/home.html")

# Member Registration (Create)
def member_register(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("member_list")  # After register, go to member list
    else:
        form = MemberForm()
    return render(request, "gymapp/member_register.html", {"form": form})

# Member List (Read)
def member_list(request):
    members = Member.objects.all()
    return render(request, "gymapp/member_list.html", {"members": members})

# Plan List
def plan_list(request):
    return render(request, "gymapp/plan_list.html")

# Trainer List
def trainer_list(request):
    return render(request, "gymapp/trainer_list.html")





