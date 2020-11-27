from django.conf import settings
from django.contrib import messages, auth
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from account import helpers
from account.forms import CustomUserCreationForm
from account.models import User


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            error = False

            # send email verification now
            activation_key = helpers.generate_activation_key(username=request.POST['username'])
            subject = 'FEIRA - Account Verification'
            message = '''\n
            Please visit the following link to verify your account: \n\n
            %s://%s/account/activate/?key=%s''' % (request.scheme, request.get_host(), activation_key)

            try:
                send_mail(subject, message, settings.SERVER_EMAIL, [request.POST['email']], fail_silently=False)
                messages.info(request, 'Account created! Click on the link sent to your email to activate the account')

            except:
                error = True
                messages.info(request, 'Unable to send email verification. Please try again')

            if not error:
                u = f.save()

                u.activation_key = activation_key
                u.is_active = False
                u.is_trusty = False
                u.save()

            return redirect('account-register')

    else:
        f = CustomUserCreationForm()

    return render(request, 'account/register.html', {'form': f})


def activate_account(request):
    key = request.GET['key']
    if not key:
        raise Http404()

    r = get_object_or_404(User, activation_key=key, is_trusty=False)
    r.is_active = True
    r.save()
    r.is_trusty = True
    r.save()

    return render(request, 'account/activated.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'usuário/senha inválido')
            return redirect('login')

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
