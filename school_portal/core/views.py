from django.views.generic import TemplateView, CreateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import User
import os
from django.conf import settings
from django.http import HttpResponse

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Serve React App - REMOVED

@method_decorator(cache_page(60 * 15), name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

