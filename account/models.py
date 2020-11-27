import re

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, username, first_name, last_name, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, first_name=first_name,
                          last_name=last_name, email=email,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, first_name, last_name, email=None, password=None, **extra_fields):
        return self._create_user(username, first_name, last_name, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        user = self._create_user(username, first_name, last_name, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.is_trusty = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=15, unique=True,
                                help_text=_(
                                    'Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
                                validators=[
                                    validators.RegexValidator(
                                        re.compile('^[\\w.@+-]+$'),
                                        _('Enter a valid username.'),
                                        _('invalid'))])
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. \
                    Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    activation_key = models.CharField(max_length=255, default=1,
                                      help_text=_('Activation code used on account creation.'))
    is_trusty = models.BooleanField(_('Validated'), default=False,
                                    help_text=_('Designates whether this user has confirmed his account.'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = f"{self.first_name}, {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
