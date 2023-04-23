from django.contrib.auth import authenticate, get_user_model, login
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from .models import BlogUser, BlogPost

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
    fields = ["email", "bio", "avatar", "website"]
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy("blog:home")

    def get_object(self, queryset=None):
        user = self.request.user
        return user.bloguser

    def form_valid(self, form):
        if self.request.user != self.get_object().user:
            raise PermissionDenied("You do not have permission to update this profile.")
        return super().form_valid(form)


class UserProfile(generic.DetailView):
    model = BlogUser
    template_name = "registration/profile.html"
    slug_field = 'user__username'
    slug_url_kwarg = 'username'

    def get_object(self, queryset=None):
        username = self.kwargs.get(self.slug_url_kwarg)
        user = get_object_or_404(BlogUser, user__username=username)
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        posts = BlogPost.objects.filter(author=user.user, is_published=True)
        drafts = BlogPost.objects.filter(author=user.user, is_published=False)
        context['posts'] = posts
        context['drafts'] = drafts
        return context


def home(request):
    if request.user.is_authenticated:
        logged_in_user = request.user
        context = {'user': logged_in_user}
    else:
        context = {'user': None}
    return render(request, 'blog/home.html', context)


class BlogPostCreateView(LoginRequiredMixin, generic.CreateView):
    model = BlogPost
    template_name = 'blog/blogpost_create.html'
    fields = ['title', 'text', 'image']
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        text = form.cleaned_data.get('text')
        if text:
            form.instance.short_description = text[:50] + '...' if len(text) > 50 else text
        if 'publish' in self.request.POST:
            form.instance.is_published = True
        return super().form_valid(form)


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        username = self.kwargs.get('username')
        blogpost = get_object_or_404(BlogPost, pk=pk, author__username=username)
        return blogpost


class BlogPostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = BlogPost
    fields = ['title', 'text']
    template_name = 'blog/blogpost_update.html'
    success_url = reverse_lazy('blog:home')

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        username = self.kwargs.get('username')
        blogpost = get_object_or_404(BlogPost, pk=pk, author__username=username)
        return blogpost

    def form_valid(self, form):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("You do not have permission to update this blog post.")
        form.instance.author = self.request.user
        text = form.cleaned_data.get('text')
        if text:
            form.instance.short_description = text[:50] + '...' if len(text) > 50 else text
        if 'publish' in self.request.POST:
            form.instance.is_published = True
        return super().form_valid(form)
