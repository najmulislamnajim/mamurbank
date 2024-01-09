from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserProfileUpdateForm
from django.contrib.auth import login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy

# Create your views here.
class UserRegistrationView(FormView):
    template_name='account/registration_form.html'
    form_class=UserRegistrationForm
    success_url=reverse_lazy('home')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request,user)
        print(user)
        return super().form_valid(form)
    
class LogInView(LoginView):
    template_name='account/user_login.html'
    def get_success_url(self):
        return reverse_lazy('home') 
    
class LogOutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')

class UserBankAccountUpdateView(View):
    template_name = 'account/profile.html'

    def get(self, request):
        form = UserProfileUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
        return render(request, self.template_name, {'form': form})
    