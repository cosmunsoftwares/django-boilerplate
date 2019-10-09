import os
from uuid import uuid4
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


def get_storage_path(filename, subdir):
    _, ext = os.path.splitext(filename)
    new_name = '{}{}'.format(str(uuid4()), ext)
    return os.path.join(subdir, new_name)


class StaticStorage(S3Boto3Storage):
    bucket_name = settings.STATIC_AWS_BUCKET


class MediaStorage(S3Boto3Storage):
    bucket_name = settings.MEDIA_AWS_BUCKET
