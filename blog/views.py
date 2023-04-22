from django.contrib.auth import authenticate, get_user_model, login
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import BlogUser

User = get_user_model()


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("blog:home")

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data.get("password1"))
        login(self.request, user)
        blog_user = BlogUser(user=user)
        blog_user.save()
        return super(RegisterFormView, self).form_valid(form)


class UpdateProfile(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = BlogUser
    fields = ["first_name", "last_name", "email", "bio", "avatar", "website"]
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy("blog:home")
    success_message = "Profile updated"

    def get_object(self, queryset=None):
        user = self.request.user
        return user.bloguser


class UserProfile(LoginRequiredMixin, generic.DetailView):
    model = BlogUser
    template_name = "registration/profile.html"

    def get_object(self, queryset=None):
        user = self.request.user
        return user.bloguser


def home(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
        context = {'user': logged_in_user}
    else:
        context = {'user': None}
    return render(request, 'blog/home.html', context)

