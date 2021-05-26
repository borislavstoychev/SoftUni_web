from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from django.views.generic import ListView

from demo.models import Phones


def index(request):
    title = "bobby`s demo"
    users = User.objects.all()
    phones = Phones.objects.all()
    context = {
        "title": title,
        "user": users,
        "phones": phones
    }
    return render(request, "index.html", context)


class PhonesListView(ListView):
    model = Phones
    template_name = 'index.html'
