from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from templates_advanced.core.mixins import AnyGroupRequiredMixin, BootstrapFormMixin
from templates_advanced.profiles.forms import ProfileForm
from templates_advanced.profiles.models import Profile


@login_required
def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profiles/details.html', context)


class ProfileUpdateView(generic.UpdateView):
    model = Profile
    context_object_name = 'profile'  # your own name for the list as a template variable
    form_class = ProfileForm
    success_url = reverse_lazy('index')
    template_name = 'profiles/details.html'


