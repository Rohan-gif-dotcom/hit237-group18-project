from django.db import models
from datetime import datetime

class Youth(models.Model):
    """
    Model to store information about youth participants in the justice system
    """
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('closed', 'Closed'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    date_registered = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_registered']
        verbose_name = 'Youth'
        verbose_name_plural = 'Youths'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Case(models.Model):
    """
    Model to store court cases and case information
    """
    CASE_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
        ('appealed', 'Appealed'),
    ]
    
    CASE_TYPE_CHOICES = [
        ('offense', 'Offense'),
        ('status', 'Status Offense'),
        ('welfare', 'Welfare/Dependency'),
    ]
    
    youth = models.ForeignKey(Youth, on_delete=models.CASCADE, related_name='cases')
    case_number = models.CharField(max_length=50, unique=True)
    case_type = models.CharField(max_length=20, choices=CASE_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=CASE_STATUS_CHOICES, default='pending')
    description = models.TextField()
    court_date = models.DateField()
    judge_name = models.CharField(max_length=100, blank=True)
    outcome = models.TextField(blank=True)
    date_filed = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_filed']
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'
    
    def __str__(self):
        return f"Case {self.case_number} - {self.youth}"

