from random import randint

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator as min_length, RegexValidator
from django.db.models import CharField, ImageField, PositiveIntegerField
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class PhoneNumberValidator(RegexValidator):
	regex = r"^[9|3|7|8][0-9]{8}$"
	message = "The phone number must consist of 9 digits and start with 3, 7, 8, 9."
	code = "invalid_phone_number"


class User(AbstractUser):
	phone_number_validator = PhoneNumberValidator()
	username_validator = UnicodeUsernameValidator()

	phone_number = CharField(
		_("phone number"),
		unique=True,
		max_length=9,
		validators=[phone_number_validator],
		help_text=_("Required. User's phone number, required 9 characters."),
		error_messages={
			"unique": _("A user with that phone number already exists."),
		},
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
		},
	)

	image = ImageField(
		_("image"),
		upload_to="users/images/",
		help_text=_("User's profile image"),
		null=True,
		blank=True,
	)

	first_name = CharField(
		_("first name"), max_length=150, blank=True, validators=[min_length(3)]
	)
	last_name = CharField(
		_("last name"), max_length=150, blank=True, validators=[min_length(3)]
	)
	coins = PositiveIntegerField(_("coins"))

	REQUIRED_FIELDS = ["first_name", "last_name"]
	USERNAME_FIELD = "phone_number"

	def save(self, *args, **kwargs) -> None:
		self.username = f"{slugify(self.get_full_name())}-{randint(1000, 9999)}"
		return super().save(*args, **kwargs)

	class Meta:
		db_table = "auth_user"
