from django.shortcuts import render
from client.models import Client
from client.forms import RegistrationForm
from client.models import Client
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import DeleteView


def client(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            client = Client(
                last_name=form.cleaned_data["last_name"],
                first_name=form.cleaned_data["first_name"],
                phone=form.cleaned_data["phone"]
            )
            client.save()

    clients = Client.objects.all()
    context = {
        'clients': clients,
        'form': form
    }
    return render(request, 'client.html', context)


class ClientDelete(DeleteView):
    model = Client
