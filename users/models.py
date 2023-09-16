from django.apps import apps
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models import ImageField, CharField
from django.utils.translation import gettext_lazy as _


class PhoneNumberValidator(RegexValidator):
    regex = r'^[9|3|7|8][0-9]{8}$'
    message = 'The phone number must consist of 9 digits and start with 3, 7, 8, 9.'
    code = 'invalid_phone_number'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given phone number, email, and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        phone_number = GlobalUserModel.normalize_username(phone_number)
        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class User(AbstractUser):
    """Phone number and password are required. Other fields are optional."""

    phone_number_validator = PhoneNumberValidator()
    username_validator = UnicodeUsernameValidator()

    phone_number = CharField(
        _('phone number'),
        unique=True,
        max_length=9,
        validators=[phone_number_validator],
        help_text=_(
            "Required. User's phone number, required 9 characters."
        ),
        error_messages={
            "unique": _("A user with that phone number already exists."),
        }
    )

    username = CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        blank=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        }
    )
    image = ImageField(
        _('image'), upload_to='users/images/',
        help_text=_('User\'s profile image'),
        null=True, blank=True
    )

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone_number'

    class Meta:
        db_table = 'auth_user'
        # Add model user into auth's tab
        # app_label = 'auth'
