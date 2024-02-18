from django.shortcuts import render
from .forms import singupforms

def sign_in(request):
    if request.method == 'POST':
        fm = singupforms(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = singupforms()
    return render(request, 'singIn/index.html', {'form':fm})
