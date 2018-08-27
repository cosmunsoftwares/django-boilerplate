from django.apps import AppConfig
from auditlog.apps import AuditlogConfig
from django.utils.translation import ugettext_lazy as _


class AuditlogCustomConfig(AuditlogConfig):
    verbose_name = _('Auditing')


class CoreConfig(AppConfig):
    name = 'project_name.core'
