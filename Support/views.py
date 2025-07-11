from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import Support,Answer
from django.db.models import Q

# Create your views here.
def support_view(request):
    msgs = Support.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        support = Support(name=name, email=email, message=message)
        support.save()
        messages.success(request,"Your message has been sent successfully!")
        return render(request, 'support.html', {'success': True})
    return render(request, 'support.html',{'msgs':msgs})

        
def answer_view(request,pk):
    message = get_object_or_404(Support,pk=pk)
    answers = Answer.objects.filter(Q(support=pk))
    if request.method == "POST" and message:
        answer = request.POST.get('answer')
        Answer.objects.create(answer=answer,support=message)

        messages.success(request,"Success!!")
    return render(request,'answer.html',{'message':message,'answers':answers})   

               
        
        