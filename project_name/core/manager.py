from django.db import models
from django.utils import timezone
from project_name.core.signals import post_soft_delete


class QuerySet(models.query.QuerySet):

    def delete(self):
        self.update(deleted_at=timezone.now())
        [post_soft_delete.send(sender=type(obj), instance=obj, using=obj._state.db) for obj in self]


class Manager(models.Manager):

    def get_queryset(self):
        return QuerySet(self.model, using=self._db).filter(deleted_at__isnull=True)
