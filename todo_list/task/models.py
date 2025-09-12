from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(
        User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="tasks"
    )
    title = models.CharField(_("Task title"), max_length=50)
    description = models.CharField(_("Task description"), max_length=255)
    is_done = models.BooleanField(_("Is done"), default=False)
    dead_line = models.DateTimeField(
        _("Task dead line time"), auto_now=False, auto_now_add=False
    )
    is_active = models.BooleanField(_("Is valid"), default=True)

    def __str__(self):
        return self.title + " | is valid : " + str(self.is_done)
