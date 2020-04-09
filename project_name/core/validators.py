import os
from django.core.exceptions import ValidationError


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('Arquivo muito grande! O tamanho não deve exceder 2 MiB.')


def file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.png', '.jpeg', '.jpg']

    if not ext.lower() in valid_extensions:
        raise ValidationError('Extensão de arquivo não suportada.')
