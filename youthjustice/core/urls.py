from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home and Dashboard
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Youth URLs
    path('youth/', views.YouthListView.as_view(), name='youth_list'),
    path('youth/new/', views.YouthCreateView.as_view(), name='youth_create'),
    path('youth/<int:pk>/', views.YouthDetailView.as_view(), name='youth_detail'),
    path('youth/<int:pk>/edit/', views.YouthUpdateView.as_view(), name='youth_update'),
    
    # Case URLs
    path('cases/', views.CaseListView.as_view(), name='case_list'),
    path('cases/new/', views.CaseCreateView.as_view(), name='case_create'),
    path('cases/<int:pk>/', views.CaseDetailView.as_view(), name='case_detail'),
    path('cases/<int:pk>/edit/', views.CaseUpdateView.as_view(), name='case_update'),
]
