
# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import SignupForm, SigninForm

class SignupView(FormView):
    template_name = 'authentication/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('signin')  # Redireciona para a página de login após sucesso

    def form_valid(self, form):
        user = form.save()
        # Ensure the 'alunos' group exists
        group_name = 'alunos'
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)  # Add user to the 'alunos' group
        return super().form_valid(form)

class SigninView(FormView):
    template_name = 'authentication/signin.html'
    form_class = SigninForm
    success_url = reverse_lazy('homePage')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('homePage')