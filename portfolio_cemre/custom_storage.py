from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage


    class MediaStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'


    class DocumentStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'


    class ImageSettingStorage(FileSystemStorage):
        file_overwrite = False
        default_acl = 'public-read'

else:
    from storages.backends.s3boto3 import S3Boto3Storage


    class MediaStorage(S3Boto3Storage):
        location = 'media'
        file_overwrite = False
        default_acl = 'public-read'


    class DocumentStorage(S3Boto3Storage):
        location = 'media/documents'
        file_overwrite = False
        default_acl = 'public-read'


    class ImageSettingStorage(S3Boto3Storage):
        location = 'media/image_settings'
        file_overwrite = False
        default_acl = 'public-read'
