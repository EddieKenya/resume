from django.shortcuts import render, redirect
from .models import Contacts, UserModel
from django.contrib import messages
# Create your views here.
def base(request):
    context = {
        'feeds' : UserModel.objects.get(id=1)
    }
    return render(request, "index.html" , context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST ['email']
        message = request.POST ['message']
        contact = Contacts.objects.create(name = name , email = email, message= message)
        contact.save()
        messages.info(request, 'Thank you for reviewing my portfolio, Message sent...')
        return redirect('base')
    else:
        return render(request, "contact.html")
