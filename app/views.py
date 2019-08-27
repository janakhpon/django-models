from django.shortcuts import render
from app.models import User

def index(request):
    return render(request, 'app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    users_dict = {'users':user_list}
    return render(request, 'app/list.html', context=users_dict)
