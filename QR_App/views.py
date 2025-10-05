from django.shortcuts import render
from django.contrib import messages
from .utils import MakeQR


def home_view(request):
    url = ""
    qr = None
    name = "qrcode"
    if request.method == 'POST':
        form_type = request.POST.get("form_type")
        if form_type == "form1":
            url = request.POST.get('url')        
            fill_color = request.POST.get('fill_color', '#000000')
            back_color = request.POST.get('back_color', '#ffffff')
            qr = MakeQR(url, fill_color, back_color)
            messages.success(request, 'QR code is generated successfully!')
        elif form_type == "form2":
            print("in form 2")
            name = request.POST.get('name')

    
    context = {
        "qr": qr,
        "url": url,
        "name": name,

    }
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html')