from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Youth, Case
from django.contrib import messages

def home(request):
    """Home page view with dashboard statistics"""
    total_youth = Youth.objects.count()
    active_youth = Youth.objects.filter(status='active').count()
    total_cases = Case.objects.count()
    pending_cases = Case.objects.filter(status='pending').count()
    
    context = {
        'total_youth': total_youth,
        'active_youth': active_youth,
        'total_cases': total_cases,
        'pending_cases': pending_cases,
    }
    return render(request, 'core/home.html', context)

def dashboard(request):
    """Dashboard view with statistics and recent data"""
    # Query all data
    youth_list = Youth.objects.all()[:5]  # Latest 5 youths
    recent_cases = Case.objects.all()[:5]  # Latest 5 cases
    
    # Statistics
    stats = {
        'total_youth': Youth.objects.count(),
        'active_youth': Youth.objects.filter(status='active').count(),
        'total_cases': Case.objects.count(),
        'pending_cases': Case.objects.filter(status='pending').count(),
        'resolved_cases': Case.objects.filter(status='resolved').count(),
    }
    
    context = {
        'youth_list': youth_list,
        'recent_cases': recent_cases,
        'stats': stats,
    }
    return render(request, 'core/dashboard.html', context)


class YouthListView(ListView):
    """List all youth with filtering and search"""
    model = Youth
    template_name = 'core/youth_list.html'
    context_object_name = 'youths'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Youth.objects.all()
        status = self.request.GET.get('status')
        search = self.request.GET.get('search')
        
        if status:
            queryset = queryset.filter(status=status)
        if search:
            queryset = queryset.filter(
                first_name__icontains=search) | queryset.filter(
                last_name__icontains=search) | queryset.filter(
                contact_number__icontains=search
            )
        return queryset.order_by('-date_registered')


class YouthCreateView(CreateView):
    """Create a new youth record"""
    model = Youth
    template_name = 'core/youth_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'email', 'address', 'status']
    success_url = reverse_lazy('core:youth_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Youth record created successfully!')
        return super().form_valid(form)


class YouthDetailView(DetailView):
    """View detailed youth information and their cases"""
    model = Youth
    template_name = 'core/youth_detail.html'
    context_object_name = 'youth'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = self.object.cases.all()
        return context


class YouthUpdateView(UpdateView):
    """Update youth information"""
    model = Youth
    template_name = 'core/youth_form.html'
    fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'contact_number', 'email', 'address', 'status']
    success_url = reverse_lazy('core:youth_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Youth record updated successfully!')
        return super().form_valid(form)


class CaseListView(ListView):
    """List all cases with filtering"""
    model = Case
    template_name = 'core/case_list.html'
    context_object_name = 'cases'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Case.objects.select_related('youth')
        status = self.request.GET.get('status')
        case_type = self.request.GET.get('case_type')
        
        if status:
            queryset = queryset.filter(status=status)
        if case_type:
            queryset = queryset.filter(case_type=case_type)
        return queryset.order_by('-date_filed')


class CaseCreateView(CreateView):
    """Create a new case"""
    model = Case
    template_name = 'core/case_form.html'
    fields = ['youth', 'case_number', 'case_type', 'status', 'description', 'court_date', 'judge_name', 'outcome']
    success_url = reverse_lazy('core:case_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Case created successfully!')
        return super().form_valid(form)


class CaseDetailView(DetailView):
    """View detailed case information"""
    model = Case
    template_name = 'core/case_detail.html'
    context_object_name = 'case'


class CaseUpdateView(UpdateView):
    """Update case information"""
    model = Case
    template_name = 'core/case_form.html'
    fields = ['youth', 'case_number', 'case_type', 'status', 'description', 'court_date', 'judge_name', 'outcome']
    success_url = reverse_lazy('core:case_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Case updated successfully!')
        return super().form_valid(form)

