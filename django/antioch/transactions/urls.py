from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions, name='transactions-list'),
    path('<str:fit_id>/', views.transaction_details, name='transaction-detail'),
    ]