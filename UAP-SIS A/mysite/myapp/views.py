# contacts/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import FeedbackForm

def contact_view(request):
    """
    Show contact form and save feedback. Optionally send an email to site admin.
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()  # save to DB
            # Optional: send notification email to site admins
            try:
                send_mail(
                    subject=f"New feedback: {feedback.subject or 'No subject'}",
                    message=f"From: {feedback.name} <{feedback.email}>\n\n{feedback.message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[admin[1] for admin in settings.ADMINS] if getattr(settings, 'ADMINS', None) else [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                # fail silently in production or log if needed
                pass

            messages.success(request, "Thank you — your message was submitted.")
            return redirect(reverse('contacts:contact'))
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = FeedbackForm()

    return render(request, 'contacts/contact.html', {'form': form})
