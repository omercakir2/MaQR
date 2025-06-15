from django.shortcuts import render
from django.contrib import messages
from .utils import MakeQR


def home_view(request):
    url = ""
    qr = None
    if request.method == 'POST':
        url = request.POST.get('url')        
        fill_color = request.POST.get('fill_color', '#000000')
        back_color = request.POST.get('back_color', '#ffffff')
        qr = MakeQR(url, fill_color, back_color)
        messages.success(request, 'QR code is generated successfully!')
    
    context = {
        "qr": qr,
        "url": url,
    }
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html')