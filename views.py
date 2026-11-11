from django.shortcuts import render
from .models import UserGreeting

def index(request):
    error = None
    greeting_name = None

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if not name:
            error = "Пожалуйста, введите ваше имя перед отправкой."
        else:
            UserGreeting.objects.create(name=name)
            greeting_name = name

    last_user = UserGreeting.objects.last()
    if not greeting_name and last_user:
        greeting_name = last_user.name

    return render(request, 'index.html', {
        'greeting_name': greeting_name,
        'error': error
    })
