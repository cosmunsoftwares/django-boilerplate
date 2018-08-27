"""This module contains the Manager class."""
from django.db import models


class Manager(models.Manager):
    """Custom Manager of the Django ORM.

    This Manager implements logic exclusion. A record is considered excluded
    when the deleted field is filled in.
    """

    def get_queryset(self, *args, **kwargs):
        """Return a Queryset.

        Return just records where deleted field is null (not excluded).
        """
        return super().get_queryset().filter(deleted_at__isnull=True)
