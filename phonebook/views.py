from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.shortcuts import redirect

from .models import Contact
from .forms import ContactCreateForm

# Create your views here

class ListContactView(ListView):
    model = Contact
    template_name = 'contact_list.html'

# class CreateContactView(CreateView):
# 	model = Contact
# 	template_name = 'edit_contact.html'

# 	def get_success_url(self):
# 		return reverse('contacts-list')

class ContactDetail(DetailView):
    model = Contact
    template_name = 'phonebook/contact-details.html'

def create_contact(request):
    if request.method == 'POST':
        create_contact_form = ContactCreateForm(request.POST)
        if create_contact_form.is_valid():
            contact = create_contact_form.save()
            return redirect('contacts-list')
    else:
        create_contact_form = ContactCreateForm()

    return render(request, 'phonebook/edit_contact.html', {
        'create_contact_form': create_contact_form,
    })

