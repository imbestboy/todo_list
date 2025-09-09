from django.db import models
import re
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core import validators


class UsernameValidator(validators.RegexValidator):
    regex = r"^(?=.{4,24}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$"
    message = _(
        "Enter a valid username. This value may contain only English letters, "
        "numbers, and . and _ characters."
        "NOTE : . and _ shouldn't at the beginning or end"
        "NOTE 2 : between _ and . should be characters"
        "NOTE 3 : username should be 5 to 24 characters"
    )
    flags = re.ASCII


class User(AbstractUser):
    email = models.EmailField(_("email address"))
    username_validator = UsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=25,
        unique=True,
        help_text=_("Required. 5 - 24 characters. Letters, digits and . and _ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
            "invalid": _(
                "NOTE : . or _ shouldn't at the beginning or end"
                "NOTE 2 : between _ and . should be characters"
                "NOTE 3 : username should be 5 to 24 characters"
            ),
        },
    )
    first_name = models.CharField(
        _("first name"),
        max_length=25,
        help_text=_("Required. 5 - 24 characters. Letters and space only."),
        error_messages={
            "invalid": _("NOTE : First name can be letters and space only"),
        },
    )
    last_name = models.CharField(
        _("last name"),
        max_length=25,
        blank=True,
        help_text=_("Required. 5 - 24 characters. Letters and space only."),
        error_messages={
            "invalid": _("NOTE : Last name can be letters and space only"),
        },
    )

    @property
    def get_full_name(self):
        return super().get_full_name()
