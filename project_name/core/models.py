from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class AbstractBaseModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(verbose_name='UUID', default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)
