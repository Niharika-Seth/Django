# create views
from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm

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

# For Update Operation
def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'gymapp/member_update.html', {'form': form})

# For Delete Operation
def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        return redirect('member_list')
    return render(request, 'gymapp/member_delete.html', {'member': member})

# Create login view
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')   # redirect after login
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'gymapp/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')   # redirect to login after logout








