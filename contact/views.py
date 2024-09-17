from django.shortcuts import render, redirect

from .models import ContactBook 
from .forms import ContactForm 

from django.views import View
from django.db.models import Q


def contact_list(request):
    name = request.GET.get('search')
    if name:
        contacts = ContactBook.objects.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name) | Q(email__icontains=name) | Q(phone_number__icontains=name))
        return render(request, 'contact/contact_list.html', {'contact_list': contacts})
    
    contacts = ContactBook.objects.all()
    return render(request, 'contact/contact_list.html', {'contact_list': contacts})

def contact_detail(request, id):
    contact = ContactBook.objects.get(id=id)
    return render(request, 'contact/contact_detail.html', {'contact': contact})

def contact_create(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    return render(request, 'contact/create_contact.html', {'form': form})


def contact_update(request, id):
    contact = ContactBook.objects.get(id=id)
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', id=id)
    return render(request, 'contact/update_contact.html', {'form': form})


def contact_delete(request, id):
    contact = ContactBook.objects.get(id=id)
    contact.delete()
    return redirect('contact_list')
