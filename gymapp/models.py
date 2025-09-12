from django.db import models

# Gym Membership Plans
class Plan(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Monthly", "Yearly"
    price = models.DecimalField(max_digits=8, decimal_places=2)  # e.g., 1500.00
    duration_months = models.IntegerField()  # e.g., 1, 12

    def __str__(self):
        return f"{self.name} - ₹{self.price}"


# Trainers
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)  # e.g., "Yoga", "Weightlifting"
    experience_years = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Gym Members
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

