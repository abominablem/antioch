from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_view, name='import'),
    path('import_ofx/', views.import_ofx, name='import-ofx'),
    ]