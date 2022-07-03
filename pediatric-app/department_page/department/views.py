from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import DataMixin


class GeneralHome(DataMixin, ListView):
    model = General
    template_name = 'department/index.html'
    context_object_name = 'general'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GeneralHome, self).get_context_data(**kwargs)
        context['posts'] = News.objects.all()
        c_def = self.get_user_context(title='Кафедра педиатрии')
        return dict(list(context.items()) + list(c_def.items()))


class NewsHome(DataMixin, ListView):
    model = News
    template_name = 'department/includes/post_news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Новости")
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'department/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class TableHome(LoginRequiredMixin, DataMixin, ListView):
    model = Articles
    template_name = 'department/timetables.html'
    context_object_name = 'table'
    login_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Расписание')
        return dict(list(context.items()) + list(c_def.items()))


class Wrapper(LoginRequiredMixin, DataMixin, ListView):
    template_name = 'department/timetables.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Расписание')
        return dict(list(context.items()) + list(c_def.items()))


class SignupUser(DataMixin, CreateView):
    form_class = SignupUserForm
    template_name = 'department/signupuser.html'
    success_url = reverse_lazy('loginuser')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'department/loginuser.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


class SotrHome(DataMixin, ListView):
    model = Sotr
    template_name = 'department/employees.html'
    context_object_name = 'employ'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = News.objects.all()
        c_def = self.get_user_context(title='Сотрудники')
        return dict(list(context.items()) + list(c_def.items()))


