from django.shortcuts import render, redirect
from .forms import FeedbackForm

def contact_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student3/thankyou.html')  # after submitting
    else:
        form = FeedbackForm()
    return render(request, 'student3/contact.html', {'form': form})
