from django.contrib import messages
from django.shortcuts import render
from .models import Support

# Create your views here.
def support_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        support = Support(name=name, email=email, message=message)
        support.save()
        messages.success(request,"Your message has been sent successfully!")
        return render(request, 'support.html', {'success': True})
    return render(request, 'support.html')

        
        