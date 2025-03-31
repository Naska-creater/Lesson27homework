from django.shortcuts import render, redirect
from .forms import UserInputForm

def input_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()  # Сохранение данных в базе данных
            return redirect('success')  # Перенаправление на страницу успешной отправки
    else:
        form = UserInputForm()
    return render(request, 'task3/input_form.html', {'form': form})

