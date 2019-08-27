from django.shortcuts import render
from app.forms import NewUser

def index(request):
    return render(request, 'app/index.html')

def users(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR ON VALIDATE')

    return render(request, 'app/list.html', {'form':form})
