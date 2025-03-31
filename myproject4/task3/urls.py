from django.urls import path
from .views import input_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', input_view, name='input_form'),
    path('success/', TemplateView.as_view(template_name='task3/success.html'), name='success'),
]

