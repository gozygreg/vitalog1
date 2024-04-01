from django.shortcuts import render, redirect
from .forms import WaitlistForm

def join_waitlist(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waitlist:success')
    else:
        form = WaitlistForm()
    return render(request, 'waitlist/join_waitlist.html', {'form': form})

def waitlist_success(request):
    return render(request, 'waitlist/waitlist_success.html')

