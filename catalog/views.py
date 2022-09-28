from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from .forms import UserRegistrationForm, ApplicationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Application
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .filters import ApplicationFilter


# Create your views here.
def index(request):
    num_applications_i = Application.objects.all().filter(status='i').count()

    return render(request, 'catalog/index.html', context={'num_applications_i': num_applications_i})


def profile(request):
    return render(request, 'catalog/profile.html',)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


class ApplicationList(generic.ListView):
    model = Application
    paginate_by = 4
    context_object_name = 'application_list'
    #Не могу выдать весь список на главную страницу


class LoanedApplicationsByUserListView(LoginRequiredMixin, generic.ListView):
    model = Application
    template_name = "catalog/application_list_borrowed_user.html"
    context_object_name = 'user_application_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ApplicationFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Application.objects.filter(borrower=self.request.user)


class ApplicationDetailView(generic.DetailView):
    model = Application


class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = "catalog/application_form.html"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        fields = form.save(commit=True)
        fields.borrower = self.request.user
        fields.save()
        return super().form_valid(form)


class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    success_url = reverse_lazy('my-applications')
