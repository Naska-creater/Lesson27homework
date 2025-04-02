from django.urls import path
from .views import UserInputFormView
from django.views.generic import TemplateView

urlpatterns = [
    path('form/', UserInputFormView.as_view(), name='form'),
    path('success/', TemplateView.as_view(template_name='task3/success.html'), name='success'),
]

