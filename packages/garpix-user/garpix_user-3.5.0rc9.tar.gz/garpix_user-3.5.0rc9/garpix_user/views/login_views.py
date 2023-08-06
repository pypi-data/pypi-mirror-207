import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic.base import RedirectView
from django.views.generic import FormView
from django.http import HttpResponse
from garpix_user.forms import LoginForm


class LogoutView(RedirectView):
    def get_redirect_url(self):
        logout(self.request)
        return self.url


class LoginView(FormView):

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if not kwargs.get('data'):
            kwargs['data'] = json.loads(getattr(self.request, 'body') or b'{}')
        return kwargs

    @staticmethod
    def get_form_class(**kwargs):
        return LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        request = self.request
        data = form.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username.lower(), password=password)
        if user:
            user.set_user_session(request)
        login(request, user)
        if self.request.accepts('text/html'):
            return redirect(request.GET.get('next', '/'))
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        if self.request.accepts('text/html'):
            return self.render_to_response(self.get_context_data(form=form))
        return HttpResponse(json.dumps(form.errors), content_type='application/json', status=400)
