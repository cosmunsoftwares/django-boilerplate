from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from project_name.core.manager import Manager
from project_name.core.signals import post_soft_delete


class AbstractBaseModel(models.Model):

    class Meta:
        abstract = True

    uuid = models.UUIDField(verbose_name='UUID', default=uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Updated at'), auto_now=True)
    deleted_at = models.DateTimeField(verbose_name=_('Deleted at'), null=True, blank=True)
    objects = Manager()
    objects_all = models.Manager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        post_soft_delete.send(sender=type(self), instance=self, using=self._state.db)

    def __str__(self):
        return str(self.pk)
