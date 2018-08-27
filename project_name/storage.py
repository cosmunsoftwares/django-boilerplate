from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    bucket_name = settings.STATIC_AWS_BUCKET


class MediaStorage(S3Boto3Storage):
    bucket_name = settings.MEDIA_AWS_BUCKET
