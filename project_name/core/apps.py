from suit.apps import DjangoSuitConfig
from auditlog.apps import AuditlogConfig

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AuditlogCustomConfig(AuditlogConfig):
    verbose_name = _('Auditing')


class CoreConfig(AppConfig):
    name = 'project_name.core'
    verbose_name = 'Configurações'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
