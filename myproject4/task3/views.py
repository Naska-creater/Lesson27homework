from django.shortcuts import render, redirect
from django.views import View

from .forms import UserInputForm

class UserInputFormView(View):

    def get (self, request, *args, **kwargs):
            form = UserInputForm()
            return render(request, 'task3/input_form.html', {'form': form})

    def post (self, request, *args, **kwargs):
            form = UserInputForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect ('success')
            return render(request, 'task3/input_form.html', {'form': form})
