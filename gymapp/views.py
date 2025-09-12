# Create view 
from django.shortcuts import render, redirect
from .models import Plan, Trainer, Member
from .forms import MemberForm

# List views
def home(request):
    return render(request, 'gymapp/home.html')


def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'gymapp/plan_list.html', {'plans': plans})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'gymapp/trainer_list.html', {'trainers': trainers})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'gymapp/member_list.html', {'members': members})

# Member registration view

def member_register(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')  # Redirect to members list
    else:
        form = MemberForm()
    return render(request, 'gymapp/member_register.html', {'form': form})



