from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    title = models.CharField(_("Task title"), max_length=50)
    description = models.CharField(_("Task description"), max_length=255)
    is_done = models.BooleanField(_("Is done"), default=False)
    dead_line = models.DateTimeField(
        _("Task dead line time"), auto_now=False, auto_now_add=False
    )
    is_active = models.BooleanField(_("Is valid"))

    def __str__(self):
        return self.title + " | is valid : " + self.is_done
